import hashlib
import random
import string
import time

def solve_crypto_puzzle_with_pattern(B):
    #generate a random pattern P of B bits
    pattern_P = ''.join(random.choices(['0', '1'], k=B))
    attempts = 0
    while True:
        #generate a random message
        message = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        #compute SHA-256 hash
        hash_hex = hashlib.sha256(message.encode()).hexdigest()
        #convert the last B bits of the hash into binary
        hash_binary = bin(int(hash_hex, 16))[-B:]
        attempts += 1
        #check if the last B bits match the pattern P
        if hash_binary == pattern_P:
            return attempts, pattern_P

#define the B values and number of trials
B_values = [4, 8, 12, 16]
trials = 10
times = []
patterns = []

#run the experiment for each B value
for B in B_values:
    start_time = time.time()
    for _ in range(trials):
        attempts, pattern_P = solve_crypto_puzzle_with_pattern(B)
    end_time = time.time()
    #calculate the average time taken for this B value
    avg_time = (end_time - start_time) / trials
    times.append(avg_time)
    patterns.append(pattern_P)  #save the pattern used for this B value

#print the results
for B, avg_time, pattern in zip(B_values, times, patterns):
    print(f'B={B}: Average Time = {avg_time:.6f} seconds, Pattern P = {pattern}')
