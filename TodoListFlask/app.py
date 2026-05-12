import requests

from flask import Flask, render_template, request, redirect, url_for

url = "https://szxaarjqdvgbsmmmernl.supabase.co/rest/v1/Tasks"
headers = {
    "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN6eGFhcmpxZHZnYnNtbW1lcm5sIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc5MTM5NzUsImV4cCI6MjA5MzQ4OTk3NX0.gZokTd52piQIsrr_NpgPgqB_PPt0PguuPwSggYMoyc8",
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN6eGFhcmpxZHZnYnNtbW1lcm5sIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc5MTM5NzUsImV4cCI6MjA5MzQ4OTk3NX0.gZokTd52piQIsrr_NpgPgqB_PPt0PguuPwSggYMoyc8"
}
app = Flask(__name__)

def get_list():
    response = requests.get(url=url, headers=headers)
    return response.json()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        due_date = request.form.get('due-date')

        print(due_date)

        new_task_data = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False  # Default value for new tasks
        }

        response = requests.post(url=url, headers=headers, json=new_task_data)

        print(response)

        return redirect(url_for('index'))
    tasks = get_list()
    print(tasks)
    return render_template("index.html", list=tasks)


if __name__ == "__main__":
    app.run(debug=True)
