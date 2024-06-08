# Define a class for a browser history, using a list as a stack
class BrowserHistory:
    # Initialize the browser history with a homepage
    def __init__(self, homepage: str):
        self.i = 0  # The current index in the history
        self.len = 1  # The length of the history
        self.history = [homepage]  # The history, starting with the homepage

    # Visit a new URL
    def visit(self, url: str) -> None:
        # If the history is not long enough to accommodate the new page
        if len(self.history) < self.i + 2:
            # Append the new page to the history
            self.history.append(url)
        else:
            # Otherwise, replace the next page in the history with the new page
            self.history[self.i + 1] = url
        # Move to the new page
        self.i += 1
        # Update the length of the history
        self.len = self.i + 1

    # Go back a certain number of pages
    def back(self, steps: int) -> str:
        # Move back a certain number of pages, but not past the beginning of the history
        self.i = max(0, self.i - steps)
        # Return the current URL
        return self.history[self.i]

    # Go forward a certain number of pages
    def forward(self, steps: int) -> str:
        # Move forward a certain number of pages, but not past the end of the history
        self.i = min(self.len - 1, self.i + steps)
        # Return the current URL
        return self.history[self.i]