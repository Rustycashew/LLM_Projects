import requests
from bs4 import BeautifulSoup
import ollama 

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

MODEL = "llama3.2:1b"

class Website:
    url : str
    title : str
    text : str


    def __init__(self,url):
        self.url = url
        response = requests.get(url , headers=headers )
        soup = BeautifulSoup(response.content , 'html.parser')
        if soup.title:
            self.title = soup.title.string
        else:
            self.title = "No title found"            
        for irrelevant in soup.body(["script" , "style" , "img" , "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="", strip=True)    




system_prompt = """
You are an assistant who analyzes the contents of a given website and provide a short on poin t summary of it , while ignoring any 
navigation related text. Respond in markdown. Do not wrap it around codeblock, only respond in markdown."""

def user_prompt_for(website):
        user_prompt = f"You are looking at a website titles {website.title}"
        user_prompt += "\nThe contents of this website is as follows; \
        please provide a short summary of this website in markdown. \
       If it includes news or announcements, then summarize these too.\n\n"
        user_prompt += website.text
        return user_prompt


def messages_for(website):
    return [
        {"role":"system","content": system_prompt},
        {"role":"user","content": user_prompt_for(website)}
    ]



def summarize(url):
    website =  Website(url)
    messages = messages_for(website)
    
    response = ollama.chat(
        model = "llama3.2:1b",
        messages = messages
    )

    return response['message']['content']



def display_summary(url):
    summary = summarize(url)
    print(summary)


s = input("Enter the website URL you want to summarise : ")

if s == "":
    print("Enter a valid website")
else:
    display_summary(s)    


