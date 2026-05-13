def generate_matrix(key):

    key = key.upper().replace("J", "I")

    matrix = []
    used = set()

    for char in key:

        if char.isalpha() and char not in used:
            used.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":

        if char not in used:
            matrix.append(char)

    matrix_5x5 = []

    for i in range(0, 25, 5):
        matrix_5x5.append(matrix[i:i+5])

    return matrix_5x5


def find_position(matrix, char):

    for row in range(5):
        for col in range(5):

            if matrix[row][col] == char:
                return row, col


def prepare_text(text):

    text = text.upper().replace("J", "I")

    text = ''.join(filter(str.isalpha, text))

    prepared = ""

    i = 0

    while i < len(text):

        a = text[i]

        if i + 1 < len(text):
            b = text[i + 1]
        else:
            b = 'X'

        if a == b:
            prepared += a + 'X'
            i += 1
        else:
            prepared += a + b
            i += 2

    if len(prepared) % 2 != 0:
        prepared += 'X'

    return prepared


def playfair_encrypt(text, key):

    matrix = generate_matrix(key)

    text = prepare_text(text)

    result = ""

    for i in range(0, len(text), 2):

        a = text[i]
        b = text[i + 1]

        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        # Same row
        if row1 == row2:

            result += matrix[row1][(col1 + 1) % 5]
            result += matrix[row2][(col2 + 1) % 5]

        # Same column
        elif col1 == col2:

            result += matrix[(row1 + 1) % 5][col1]
            result += matrix[(row2 + 1) % 5][col2]

        # Rectangle rule
        else:

            result += matrix[row1][col2]
            result += matrix[row2][col1]

    return result


def playfair_decrypt(text, key):

    matrix = generate_matrix(key)

    result = ""

    for i in range(0, len(text), 2):

        a = text[i]
        b = text[i + 1]

        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        # Same row
        if row1 == row2:

            result += matrix[row1][(col1 - 1) % 5]
            result += matrix[row2][(col2 - 1) % 5]

        # Same column
        elif col1 == col2:

            result += matrix[(row1 - 1) % 5][col1]
            result += matrix[(row2 - 1) % 5][col2]

        # Rectangle rule
        else:

            result += matrix[row1][col2]
            result += matrix[row2][col1]

    return result