# Database.py
from sentence_transformers import SentenceTransformer, util
import string, sqlite3, hashlib, random
from contextlib import closing

DB_PATH = "helpdesk.db"


# Load model (do this once, outside the function for speed)
model = SentenceTransformer('all-MiniLM-L6-v2')

def format_response(answer):
    """
    Converts raw database answers into a modern conversational reply.
    """
    openers = [
        "Here’s what I found:",
        "Here’s the explanation:",
        "Let me break this down for you:",
        "Sure, here’s the answer:",
        "Got it. Here's the information:",
    ]

    closers = [
        "If you want to explore something else, feel free to ask.",
        "Let me know if you'd like more details.",
        "You can ask me anything else you’re curious about.",
        "If you need help with something else, I’m here.",
    ]

    
    return f"{random.choice(openers)}\n\n{answer}\n\n{random.choice(closers)}"


def get_answer(user_question):

    # Normalize input
    user_question = user_question.lower().translate(
        str.maketrans("", "", string.punctuation)
    )

    # Connect to DB
    conn = sqlite3.connect("helpdesk.db")
    cursor = conn.cursor()

    cursor.execute("SELECT questions, answers, keywords FROM faq")
    rows = cursor.fetchall()

    conn.close()

    if not rows:
        return "I cannot confirm this because the FAQ table is empty."

    # Prepare DB text + answer list
    db_texts = []
    answers = []

    for q, a, k in rows:
        if k:
            combined = f"{q} {k}".lower().translate(
                str.maketrans("", "", string.punctuation)
            )
        else:
            combined = q.lower()

        db_texts.append(combined)
        answers.append(a)

    # Encode using the embedding model
    user_embedding = model.encode(user_question, convert_to_tensor=True)
    db_embeddings = model.encode(db_texts, convert_to_tensor=True)

    # Compute similarity scores
    similarities = util.pytorch_cos_sim(user_embedding, db_embeddings)[0]

    best_index = similarities.argmax()
    best_similarity = similarities[best_index].item()

    # Adjust threshold for best accuracy
    if best_similarity > 0.5:
        best_answer = answers[best_index]
        return format_response(best_answer)
    else:
        return "I cannot confirm this because no matching answer was found."
    





def insert_questions():
    data = [

    ]
    

    conn = sqlite3.connect("helpdesk.db")
    cursor = conn.cursor()

    cursor.executemany("""
    INSERT INTO faq (questions, answers, keywords)
    VALUES (?, ?, ?)
    """, data)

    conn.commit()
    conn.close()

    print("FAQ data inserted successfully.")


#Login Database
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def connect_db():
    return sqlite3.connect(DB_PATH)

sqlite3.connect(DB_PATH)

def init_db():
    with closing(connect_db()) as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            );
        """)
        conn.commit()

def register_user(username: str, password: str) -> bool:
    username = (username or "").strip()
    password = (password or "").strip()
    if not username or not password:
        return False

    hashed_password = hash_password(password)

    try:
        with closing(connect_db()) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False


def login_user(username: str, password: str) -> bool:
    username = (username or "").strip()
    password = (password or "").strip()
    if not username or not password:
        return False

    hashed_password = hash_password(password)

    try:
        with closing(connect_db()) as conn:
            cur = conn.cursor()
            cur.execute("SELECT id FROM users WHERE username=? AND password=?", (username, hashed_password))
            user = cur.fetchone()
        return user is not None
    except Exception:
        return False

def change_password(username, old_password, new_password):
    hashed_new = hash_password(new_password)
    hashed_old = hash_password(old_password)

    try:
        with closing(connect_db()) as conn:
            cur = conn.cursor()
            cur.execute(
                "UPDATE users SET password = ? WHERE username = ? AND password = ?",
                (hashed_new, username, hashed_old)
            )
            conn.commit()

            if cur.rowcount > 0:
                return True
            else:
                return False
    except Exception as e:
        print("Error updating password:", e)
        return False



''' 
match = re.search(r'(\d+\s*[\+\-\*/]\s*\d+)', text)
    if match:
        try:
            expression = match.group(1)
            result = eval(expression)
            return f"The answer is {result}."
        except:
            return None
    return None
'''




    
