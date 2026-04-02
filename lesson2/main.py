from google import genai
from dotenv import load_dotenv

load_dotenv()  # 會讀目前工作目錄下的 .env

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="華特固態照明公司評比"
)
print(response.text)
