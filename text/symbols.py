""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
'''
_pad = '_'
_punctuation = ';:,.!?¡¿—…"«»“” '
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
_letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"


# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)

# Special symbol ids
SPACE_ID = symbols.index(" ")


class Tokenizer():
    """
        for self-defined dataset
    """
    def __init__(self, token_path):

        tokens = []
        with open(token_path, 'r') as f:
            for line in f.readlines():
                tokens.append(line.strip())

        self._token_to_id = {s: i for i, s in enumerate(tokens)}
        self._id_to_token = {i: s for i, s in enumerate(tokens)}

    def tokenize(self, text, split_char=None):
        if split_char is not None:
            text = text.split(split_char)
        sequence = [self._token_to_id[symbol] for symbol in text]
        return sequence
        