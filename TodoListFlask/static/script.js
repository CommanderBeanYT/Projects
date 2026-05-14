document.addEventListener('DOMContentLoaded', function() {
    const checkButtons = document.querySelectorAll('.checkbox'); //get all checkboxes
    const removeButtons = document.querySelectorAll('.remove'); //get all remove buttons

    checkButtons.forEach(checkbox => {
        checkbox.addEventListener('change', function(event) {
            // once user toggles a checkbox update the database
            fetch(`https://szxaarjqdvgbsmmmernl.supabase.co/rest/v1/Tasks?id=eq.${this.id}`, {
                method: 'PATCH',
                headers: {
                    "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN6eGFhcmpxZHZnYnNtbW1lcm5sIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc5MTM5NzUsImV4cCI6MjA5MzQ4OTk3NX0.gZokTd52piQIsrr_NpgPgqB_PPt0PguuPwSggYMoyc8",
                    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN6eGFhcmpxZHZnYnNtbW1lcm5sIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc5MTM5NzUsImV4cCI6MjA5MzQ4OTk3NX0.gZokTd52piQIsrr_NpgPgqB_PPt0PguuPwSggYMoyc8",
                    "Content-Type": "application/json",
                    "Prefer": "return=minimal"
                },
                body: JSON.stringify({
                    completed: this.checked
                })
            })
        });
    });

    removeButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            // once user clicks a remove button remove it from the database

            fetch(`https://szxaarjqdvgbsmmmernl.supabase.co/rest/v1/Tasks?id=eq.${this.id}`, {
                method: 'DELETE',
                headers: {
                    "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN6eGFhcmpxZHZnYnNtbW1lcm5sIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc5MTM5NzUsImV4cCI6MjA5MzQ4OTk3NX0.gZokTd52piQIsrr_NpgPgqB_PPt0PguuPwSggYMoyc8",
                    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN6eGFhcmpxZHZnYnNtbW1lcm5sIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc5MTM5NzUsImV4cCI6MjA5MzQ4OTk3NX0.gZokTd52piQIsrr_NpgPgqB_PPt0PguuPwSggYMoyc8",
                    "Content-Type": "application/json"
                }
            }).then(
                button.parentElement.remove()
            )
        });
    });
});
