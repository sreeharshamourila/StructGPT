




ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

        raw_paragraphs = content.split('\n\n')

        # Process each paragraph to replace single newlines with spaces
        paragraphs = [' '.join(para.split('\n')) for para in raw_paragraphs if para.strip()]

        return paragraphs