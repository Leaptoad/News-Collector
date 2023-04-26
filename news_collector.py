import requests
import json
import tkinter as tk
import webbrowser
import tkinter.font as tkfont

API_KEY = '4b826cf7c46744b2b1e3c81762e5ed33'

def get_news_articles(search_term, sources=None, from_date=None, to_date=None):
    url = f"https://newsapi.org/v2/everything?q={search_term}&apiKey={API_KEY}"
    if sources:
        url += f"&sources={sources}"
    if from_date:
        url += f"&from={from_date}"
    if to_date:
        url += f"&to={to_date}"
    response = requests.get(url)
    articles = json.loads(response.content)['articles']
    return articles

def search_articles():
    search_term = entry.get()
    from_date = from_entry.get()
    to_date = to_entry.get()
    articles = get_news_articles(search_term, from_date=from_date, to_date=to_date)
    display_articles(articles)

def display_articles(articles):
    result_box.delete(0, tk.END)
    for article in articles:
        result_box.insert(tk.END, article['title'])
        result_box.insert(tk.END, article['description'])
        url = article['url']
        result_box.insert(tk.END, url)
        result_box.insert(tk.END, '')
    result_box.bind("<Button-1>", lambda event: webbrowser.open_new(result_box.get(result_box.curselection())))

if __name__ == '__main__':
    window = tk.Tk()
    window.title("News Collector")
    
    search_label = tk.Label(window, text="Search Articles:")
    search_label.grid(row=0, column=0, padx=10, pady=10)
    entry = tk.Entry(window)
    entry.grid(row=0, column=1, padx=10, pady=10)
    
    from_label = tk.Label(window, text="From Date (mm-dd-yyyy):")
    from_label.grid(row=2, column=0, padx=10, pady=10)
    from_entry = tk.Entry(window)
    from_entry.grid(row=2, column=1, padx=10, pady=10)
    
    to_label = tk.Label(window, text="To Date (mm-dd-yyyy):")
    to_label.grid(row=3, column=0, padx=10, pady=10)
    to_entry = tk.Entry(window)
    to_entry.grid(row=3, column=1, padx=10, pady=10)
    
    search_button = tk.Button(window, text="Search", command=search_articles)
    search_button.grid(row=4, column=1, padx=10, pady=10)
    
    result_label = tk.Label(window, text="Results:")
    result_label.grid(row=5, column=0, padx=10, pady=10)
    result_box = tk.Listbox(window, height=20, width=100)
    result_box.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    
    window.mainloop()
