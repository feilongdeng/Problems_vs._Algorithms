# A RouteTrie will store our routes and their associated handlers

class RouteTrie:

    def __init__(self, handler=None):

        # Initialize the trie with an root node and a handler, this is the root path or home page node

        self.root = RouteTrieNode(handler=handler)



    def insert(self, request_path, handler):

        # Similar to our previous example you will want to recursively add nodes

        # Make sure you assign the handler to only the leaf (deepest) node of this path



        # Split the path into sub paths with "/"

        sub_path_list = request_path.split("/")



        # Only process the path if there exist 1 or more sub-paths

        if len(sub_path_list) <= 1:

            return



        cur_node = self.root

        for sub_path in sub_path_list[1:]:

            # Check whether the sub path exist in this node and traverse the tree accordingly

            if sub_path in cur_node.sub_path_dict:

                cur_node = cur_node.sub_path_dict[sub_path]

            else:

                # This is a new sub-path, create a new child node and update the dictionary mapping

                child_route_trie_node = RouteTrieNode()

                cur_node.sub_path_dict[sub_path] = child_route_trie_node

                cur_node = child_route_trie_node



        # cur_node is now at the leaf node, update the handler attribute

        cur_node.handler = handler



    def find(self, request_path):

        # Starting at the root, navigate the Trie to find a match for this path

        # Return the handler for a match, or None for no match



        # Trim the trailing "/"

        if request_path[-1] == "/":

            request_path = request_path[:-1]



        # Split the path into sub path by "/"

        sub_path_list = request_path.split("/")



        cur_node = self.root



        # If there exist no or only 1 sub-path, return the root handler

        if len(sub_path_list) <= 1:

            return cur_node.handler



        # Traverse the Trie base on the list of sub paths

        for sub_path in sub_path_list[1:]:

            if sub_path in cur_node.sub_path_dict:

                cur_node = cur_node.sub_path_dict[sub_path]

            else:

                return None



        return cur_node.handler



    def __str__(self):

        output_str = [""]



        def print_node(node, output_str):

            output_str[0] += f"Node handler: {node.handler}\n"

            # print(output_str)

            for sub_path in node.sub_path_dict:

                output_str[0] += f"Sub path: {sub_path}\n"



                print_node(node.sub_path_dict[sub_path], output_str)



        print_node(self.root, output_str)



        return output_str[0]





# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.

class RouteTrieNode:

    def __init__(self, handler=None):

        # Initialize the node with children as before, plus a handler

        self.handler = handler



        # A dictionary of sub-paths to it's corresponding child RouteTrieNode

        self.sub_path_dict = dict()



    def insert(self, sub_path, handler=None):

        # Insert the node as before

        route_trie_node = RouteTrieNode(handler)

        self.sub_path_dict[sub_path] = route_trie_node





# The Router class will wrap the Trie and handle

class Router:

    def __init__(self, root_handler=None, not_found_handler=None):

        # Create a new RouteTrie for holding our routes

        # You could also add a handler for 404 page not found responses as well!

        self.route_trie = RouteTrie(handler=root_handler)

        self.not_found_handler = not_found_handler



    def add_handler(self, request_path, handler):

        # Add a handler for a path

        # You will need to split the path and pass the pass parts

        # as a list to the RouteTrie

        self.route_trie.insert(request_path, handler)



    def lookup(self, request_path):

        # lookup path (by parts) and return the associated handler

        # you can return None if it's not found or

        # return the "not found" handler if you added one

        # bonus points if a path works with and without a trailing slash

        # e.g. /about and /about/ both return the /about handler

        handler = self.route_trie.find(request_path)



        if handler is None:

            return self.not_found_handler

        else:

            return handler





# create the router and add a route

router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this

router.add_handler("/home/about", "about handler")  # add a route



# some lookups with the expected output



# Test case 1

#look up root handler with path "/"

print("Test case 1 - look up root handler with path '/'")

# should print 'root handler'

print(router.lookup("/"))


# should print 'not found handler' or None if you did not implement one

print(router.lookup("/home"))


# should print 'about handler'

print(router.lookup("/home/about"))


#Test case 2

router = Router()

print ("\nTest case 2:")

print(router.lookup("/"))  #should print None

#Test case 3

router = Router()


router.add_handler('/udacity', 'udacity')

print ("\nTest case 3:")

print(router.lookup("/"))       #should print None
print(router.lookup("/udacity")) #should print udacity
print(router.lookup("/abcd"))   #should print None
