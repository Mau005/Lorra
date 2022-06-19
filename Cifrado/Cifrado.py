import hashlib, pickle

class Cifrados():

    @classmethod
    def cifrado_sha1(cls, data):
        return hashlib.sha1(bytes(data)).hexdigest()

    @classmethod
    def cifrado_md5(cls, data):
        return hashlib.md5(bytes(data)).hexdigest()
    @classmethod
    def empaquetar(cls, data):
        return pickle.dumps(data)

    @classmethod
    def desenpaqueta(cls, data):
        return pickle.loads(data)


if __name__ == "__main__":
    test = Cifrados()
    test_objeto = {1: "Mandar esta chets"}
    test_empaquetado = test.empaquetar(test_objeto)
    print(test_empaquetado)
    test_desenpaquetado = test.desenpaqueta(test_empaquetado)
    print(test_desenpaquetado)

    contra = b"los amigos de tu hermana"
    print(test.cifrado_sha1(contra))
    print(test.cifrado_md5(contra))
