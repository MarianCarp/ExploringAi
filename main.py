import os

# Define the Spider class
class Spider:
    # Initialize the Spider with a starting URL and other necessary attributes
    def __init__(self, url):
        self.url = url  # The starting URL
        self.data = []  # List to store the crawled URLs
        self.visited = []  # List to store the visited URLs
        self.to_visit = [url]  # List of URLs to visit, starting with the initial URL
        self.depth = 0  # Current depth of the crawl
        self.max_depth = 5  # Maximum depth to crawl
        self.max_pages = 50  # Maximum number of pages to crawl
        self.file = open("data.txt", "w")  # File to write the crawled URLs
        
    # Method to start the crawl
    def crawl(self):
        # Continue crawling until there are no more URLs to visit or the maximum number of pages has been reached
        while self.to_visit and len(self.data) < self.max_pages:
            url = self.to_visit.pop(0)  # Get the next URL to visit
            # If the URL has not been visited yet
            if url not in self.visited:
                self.visited.append(url)  # Add the URL to the visited list
                self.data.append(url)  # Add the URL to the data list
                self.file.write(url + "\n")  # Write the URL to the file
                self.depth += 1  # Increase the crawl depth
                # If the maximum depth has not been reached, add the extracted URLs to the to_visit list
                if self.depth < self.max_depth:
                    self.to_visit.extend(self.extract_urls(url))
        self.file.close()  # Close the file when done crawling
        
    # Method to extract URLs from a given URL
    def extract_urls(self, url):
        # For simplicity, this method just appends a number to the given URL
        return [url + "/" + str(i) for i in range(10)]

# Create a Spider instance with the starting URL "https://coder.today"
test = Spider("https://coder.today")
# Start the crawl
test.crawl()
# Print the crawled URLs
print(repr(test.data))
# Check if the number of crawled URLs is not bigger than 50

assert len(test.data) <= 50
# Check if the number of visited URLs is not bigger than 50
assert len(test.visited) <= 50
# Check if the number of URLs to visit is 0
assert len(test.to_visit) == 0
# Check if the depth is not bigger than 5
assert test.depth <= 5
# Check if the file "data.txt" exists
assert os.path.exists("data.txt")
# Check if the file "data.txt" is not empty
assert os.path.getsize("data.txt") > 0


