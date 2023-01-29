from threading import Thread

arr=[8,3,0,2,6,4,7,5,9,6,3]
even_counter =0  #to count number of even data in even thread
odd_counter=0   #to count number of odd data in even thread

# Function for sorting even numbers
def sort_even():
    #create list
    even_numbers = []
    for x in arr:
        if (x % 2 == 0):
            even_numbers.append(x)
            global even_counter
            even_counter+=1
    even_numbers.sort()

    return even_numbers

# Function for sorting odd numbers
def sort_odd():

    odd_numbers = []
    for x in arr:
        if (x % 2 != 0):
            odd_numbers.append(x)
            global odd_counter
            odd_counter += 1
    odd_numbers.sort()
    return odd_numbers


# Function for merging the results
def merge_results():
    # Merge the two lists
    merge_list =[]
    if (even_counter >= 1): #if number of even data great than or equal
         merge_list = merge_list + sort_even()

    if (odd_counter >= 1): #if number of odd data great than or equal
         merge_list = merge_list + sort_odd()

    print("Even numbers:", sort_even())
    print("Odd numbers:", sort_odd())
    print("Merged List: ", merge_list)

    return merge_list

if __name__ == "__main__":

    even_thread = Thread(target=sort_even)
    odd_thread = Thread(target=sort_odd)
    merge_thread = Thread(target=merge_results)

    # Start the threads
    even_thread.start()
    odd_thread.start()
    merge_thread.start()

    #Wait for the threads to finish
    even_thread.join()
    odd_thread.join()
    merge_thread.join()
