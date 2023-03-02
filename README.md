# URL-shorteners
Link or URL shortening has a variety of benefits for both the company doing the shortening as well as the user of the shortened links. 
This is a Python code for a basic URL shortener GUI application using the pyshorteners and pyperclip libraries. The application uses the tkinter library for creating a graphical user interface (GUI).

The code starts by importing the required libraries, including pyperclip for copying the shortened URL to the clipboard and pyshorteners for generating the short URL. It also imports the tkinter library for GUI design.

After importing the necessary libraries, the code defines a GUI window using the Tk() method from the tkinter library. It sets the geometry, title, and background color of the window.

The code creates two string variables, url and url_address, to store the long URL and the shortened URL, respectively.

Next, the code defines two functions, urlshortener() and copyurl(), for shortening the URL and copying the shortened URL to the clipboard, respectively.

The urlshortener() function takes the input URL from the url variable, generates a short URL using the pyshorteners.Shortener().tinyurl.short() method, and stores the result in the url_address variable.

The copyurl() function retrieves the shortened URL from the url_address variable and copies it to the clipboard using the pyperclip.copy() method.

Finally, the code creates a GUI layout using the Label, Entry, and Button widgets from the tkinter library. It adds a title to the window using the Label widget, an input field for the long URL using the Entry widget, a button to generate the short URL using the Button widget, an output field for the shortened URL using the Entry widget, and a button to copy the shortened URL to the clipboard using the Button widget.

The root.mainloop() method is called at the end to start the GUI event loop and display the window on the screen.



