# Define a class for a node in a doubly linked list
class ListNode:
    # Initialize a node with a value, and optional previous and next nodes
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# Define a class for a browser history, using a doubly linked list
class BrowserHistory:
    # Initialize the browser history with a homepage
    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)  # The current page is a node with the homepage URL

    # Visit a new URL
    def visit(self, url: str) -> None:
        # Create a new node for the URL, with the current page as the previous node
        self.cur.next = ListNode(url, self.cur)
        # Move to the new page
        self.cur = self.cur.next

    # Go back a certain number of pages
    def back(self, steps: int) -> str:
        # While there are pages to go back to and steps remaining
        while self.cur.prev and steps > 0:
            # Move to the previous page
            self.cur = self.cur.prev
            # Decrease the number of steps
            steps -= 1
        # Return the current URL
        return self.cur.val

    # Go forward a certain number of pages
    def forward(self, steps: int) -> str:
        # While there are pages to go forward to and steps remaining
        while self.cur.next and steps > 0:
            # Move to the next page
            self.cur = self.cur.next
            # Decrease the number of steps
            steps -= 1
        # Return the current URL
        return self.cur.val