class Text:

    mkhedruli_alpha = [letter for letter
                       in 'აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ']
    khutsuri_alpha = [letter for letter
                      in 'ⴀⴁⴂⴃⴄⴅⴆⴇⴈⴉⴊⴋⴌⴍⴎⴏⴐⴑⴒⴓⴔⴕⴖⴖⴘⴙⴚⴛⴜⴝⴞⴟⴠ']
    asomtavruli_alpha = [letter for letter
                         in 'ႠႡႢႣႤႥႦႧႨႩႪႫႬႭႮႯႰႱႲჃႴႵႶႷႸႹႺႻႼႽႾႿჀ']

    def __init__(self, text, alphabet_type):
        self.text = text
        self.type = alphabet_type

    def convert_to_khutsuri(self):
        if self.type == 'მხედრული':
            mkhedruli_to_khutsuri = dict(zip(Text.mkhedruli_alpha,
                                             Text.khutsuri_alpha))
            khutsuri_text = self.text
            for letter in khutsuri_text:
                if letter.isalpha():
                    khutsuri_text = khutsuri_text\
                        .replace(letter, mkhedruli_to_khutsuri[letter])
            return khutsuri_text
        elif self.type == 'ასომთავრული':
            asomtavruli_to_khutsuri = dict(zip(Text.asomtavruli_alpha,
                                               Text.khutsuri_alpha))
            khutsuri_text = self.text
            for letter in khutsuri_text:
                if letter.isalpha():
                    khutsuri_text = khutsuri_text\
                        .replace(letter, asomtavruli_to_khutsuri[letter])
            return khutsuri_text

    def convert_to_asomtavruli(self):
        if self.type == 'მხედრული':
            mkhedruli_to_asomtavruli = dict(zip(Text.mkhedruli_alpha,
                                                Text.asomtavruli_alpha))
            asomtavruli_text = self.text
            for letter in asomtavruli_text:
                if letter.isalpha():
                    asomtavruli_text = asomtavruli_text\
                        .replace(letter, mkhedruli_to_asomtavruli[letter])
            return asomtavruli_text
        elif self.type == 'ხუცური':
            khutsuri_to_asomtavruli = dict(zip(Text.khutsuri_alpha,
                                               Text.asomtavruli_alpha))
            asomtavruli_text = self.text
            for letter in asomtavruli_text:
                if letter.isalpha():
                    asomtavruli_text = asomtavruli_text\
                        .replace(letter, khutsuri_to_asomtavruli[letter])
            return asomtavruli_text

    def convert_to_mkhedruli(self):
        if self.type == 'ხუცური':
            khutsuri_to_mkhedruli = dict(zip(Text.khutsuri_alpha,
                                             Text.mkhedruli_alpha))
            mkhedruli_text = self.text
            for letter in mkhedruli_text:
                if letter.isalpha():
                    mkhedruli_text = mkhedruli_text\
                        .replace(letter, khutsuri_to_mkhedruli[letter])
            return mkhedruli_text
        elif self.type == 'ასომთავრული':
            asomtavruli_to_mkhedruli = dict(zip(Text.asomtavruli_alpha,
                                                Text.mkhedruli_alpha))
            mkhedruli_text = self.text
            for letter in mkhedruli_text:
                if letter.isalpha():
                    mkhedruli_text = mkhedruli_text\
                        .replace(letter, asomtavruli_to_mkhedruli[letter])
            return mkhedruli_text
