import tkinter as tk
from tkinter import scrolledtext, ttk
from tkinter import font as tkfont
from datetime import datetime

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Chat Assistant")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)
        self.root.configure(bg='#f0f2f5')
        
        # Custom fonts
        self.title_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
        self.chat_font = tkfont.Font(family="Helvetica", size=12)
        self.input_font = tkfont.Font(family="Helvetica", size=12)
        
        self.create_widgets()
        self.setup_layout()
        
    def create_widgets(self):
        # Header frame
        self.header_frame = tk.Frame(self.root, bg='#2c3e50', height=60)
        self.header_label = tk.Label(
            self.header_frame,
            text="AI Chat Assistant",
            font=self.title_font,
            fg='white',
            bg='#2c3e50',
            pady=15
        )
        
        # Chat display area
        self.chat_display = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            font=self.chat_font,
            bg='white',
            fg='#333333',
            padx=15,
            pady=15,
            state='disabled'
        )
        self.chat_display.tag_config('user', foreground='#2c3e50', lmargin1=100, rmargin=50)
        self.chat_display.tag_config('bot', foreground='#27ae60', lmargin1=50, rmargin=100)
        self.chat_display.tag_config('time', foreground='#7f8c8d', font=('Helvetica', 8))
        
        # Input frame
        self.input_frame = tk.Frame(self.root, bg='#f0f2f5', padx=10, pady=10)
        
        self.user_input = tk.Text(
            self.input_frame,
            height=3,
            font=self.input_font,
            bg='white',
            fg='#333333',
            padx=10,
            pady=10,
            wrap=tk.WORD
        )
        
        self.send_button = ttk.Button(
            self.input_frame,
            text="Send",
            style='TButton',
            command=self.send_message
        )
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12), padding=6)
        self.style.map('TButton',
            foreground=[('pressed', 'white'), ('active', 'white')],
            background=[('pressed', '#16a085'), ('active', '#1abc9c')]
        )
        
        # Bind Enter key to send message
        self.user_input.bind('<Return>', lambda event: self.send_message())
        
    def setup_layout(self):
        # Header layout
        self.header_frame.pack(fill=tk.X)
        self.header_label.pack()
        
        # Chat display layout
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # Input layout
        self.input_frame.pack(fill=tk.X, pady=(0, 10))
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.send_button.pack(side=tk.RIGHT)
        
    def send_message(self):
        message = self.user_input.get("1.0", tk.END).strip()
        if message:
            self.display_message(message, 'user')
            self.user_input.delete("1.0", tk.END)
            # Here we would normally process the message and get a response
            # For now, we'll just echo with a simulated response
            self.root.after(1000, lambda: self.display_message(
                f"I received your message: '{message}'. This is a simulated response.", 
                'bot'
            ))
    
    def display_message(self, message, sender):
        timestamp = datetime.now().strftime("%H:%M")
        self.chat_display.config(state='normal')
        
        # Insert timestamp
        self.chat_display.insert(tk.END, f"[{timestamp}] ", 'time')
        
        # Insert message with appropriate tag
        self.chat_display.insert(tk.END, f"{message}\n\n", sender)
        
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)
        
    def run(self):
        # Display welcome message
        self.display_message("Hello! I'm your AI assistant. How can I help you today?", 'bot')
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    app.run()
