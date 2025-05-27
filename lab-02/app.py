from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Index.html")


#           CAESAR

@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

@app.route("/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return render_template("caesar.html", outputCipherText=encrypted_text)

@app.route("/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return render_template("caesar.html", outputPlainText=decrypted_text)



#           VIGENERE

@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)
    return render_template("caesar.html", outputCipherText=encrypted_text)

@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)
    return render_template("caesar.html", outputPlainText=decrypted_text)



#           RAILFENCE

@app.route("/railfence")
def railfence():
    return render_template("railfence.html")

@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    Railfence = RailFenceCipher()
    encrypted_text = Railfence.rail_fence_encrypt(text, key)
    return render_template("railfence.html", outputCipherText=encrypted_text)

@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    Railfence = RailFenceCipher()
    decrypted_text = Railfence.rail_fence_decrypt(text, key)
    return render_template("railfence.html", outputPlainText=decrypted_text)


#           PLAYFAIR

@app.route("/playfair")
def playfair():
    return render_template("playfair.html")

@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    Playfair = PlayfairCipher()
    matrix = Playfair.create_playfair_matrix(key)
    encrypted_text = Playfair.playfair_encrypt(text, matrix)
    return render_template("playfair.html", outputCipherText=encrypted_text)

@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    Playfair = PlayfairCipher()
    matrix = Playfair.create_playfair_matrix(key)
    decrypted_text = Playfair.playfair_decrypt(text, matrix)
    return render_template("playfair.html", outputPlainText=decrypted_text)



#           TRANPOSTION

@app.route("/transposition")
def transposition():
    return render_template("transposition.html")

@app.route("/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    Transposition = TranspositionCipher()
    encrypted_text = Transposition.encrypt(text, key)
    return render_template("transposition.html", outputCipherText=encrypted_text)

@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    Transposition = TranspositionCipher()
    decrypted_text = Transposition.decrypt(text, key)
    return render_template("transposition.html", outputPlainText=decrypted_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)