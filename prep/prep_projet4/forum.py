from abc import ABC

class File(ABC):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self):
        pass


class Image(File):
    def display(self):
        print(f"nom de l'image : {self.name}")

class Gif(Image):
    def display(self):
        super().display()
        print("l'image est de type GIF.")

class Jpg(Image):
    """Affiche l'image."""
    def display(self):
        super().display()
        print("L'image est de type 'jpg'.")


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"L'utilisateur {self.username} est connecté.")

    def post(self, thread, content, file=None):
        """Poste un message dans un fil de discussion."""
        if file:
            post = FilePost(self, "aujourd'hui", content, file)
        else:
            post = Post(user=self, time_posted="aujourd'hui", content=content)
        thread.add_post(post)
        return post

    def make_thread(self, title, content):
        """Créé un nouveau fil de discussion."""
        post = Post(self, "aujourd'hui", content)
        return Thread(title, "aujourd'hui", post)

    def __str__(self):
        """représentation de l'utilisateur."""
        return self.username


class Moderator(User):
    """Utilisateur modérateur."""

    def edit(self, post, content):
        """Modifie un message."""
        post.content = content

    def delete(self, thread, post):
        """Supprime un message."""
        index = thread.posts.index(post)
        del thread.posts[index]


class Post:
    def __init__(self, user, time_posted, content):
        self.user = user
        self.time_posted = time_posted
        self.content = content

    def display(self):
        """Affiche le message."""
        print(f"Message posté par {self.user} le {self.time_posted}:")
        print(self.content)



class FilePost(Post):
    """Message comportant un fichier."""

    def __init__(self, user, time_posted, content, file):
        """Initialise le fichier."""
        super().__init__(user, time_posted, content)
        self.file = file

    def display(self):
        """Affiche le contenu et le fichier."""
        super().display()
        print("pièce jointe:")
        self.file.display()


class Thread:
    """Fil de discussions."""

    def __init__(self, title, time_posted, post):
        """Initialise le titre, la date et les posts.

        Attention ici: on commence par un seul post, celui du sujet.
        Les réponses à ce post ne pourrons s'ajouter qu'ultérieurement.
        En effet, on ne créé pas directement un nouveau fil avec des réponses. ;)
        """
        self.title = title
        self.time_posted = time_posted
        self.posts = [post]

    def display(self):
        """Affiche le fil de discussion."""

        print("----- THREAD -----")
        print(f"titre: {self.title}, date: {self.time_posted}")
        print()
        for post in self.posts:
            post.display()
            print()
        print("------------------")

    def add_post(self, post):
        """Ajoute un post."""
        self.posts.append(post)

def main():
    user = User("Bob", "abc")
    modo = Moderator("mady", "456")
    nouveau_gateau = Post(user, "11h", "voici ma nouvelle recette de dingue!")
    gateau = Thread("gateau_choco", "11h", nouveau_gateau)
    gateau.display()
    rep_gateau = Post(modo, "12h", "merci beaucoup, ça a l'air top!")
    gateau.add_post(rep_gateau)
    gateau.display()
    msg3 = Post(user, "12h20", "On se voit quand ?")
    gateau.add_post(msg3)
    gateau.display()
    msg4 = Post(modo, "12h30", "hors sujet, je vais supprimer.")
    gateau.add_post(msg4)
    gateau.display()
    modo.delete(gateau, msg3)
    gateau.display()
    modo.delete(gateau, msg4)
    gateau.display()
    coeur = Image("coeur", 50)
    msg_img = FilePost(user, "13h", "pour me faire pardonner", coeur)
    gateau.add_post(msg_img)
    gateau.display()


if __name__ == "__main__":
    main()



