#  Huffman Coding
import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1
    
    heap = []
    for char, count in freq.items():
        heapq.heappush(heap, HuffmanNode(char=char, freq=count))
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)
    
    return heapq.heappop(heap)

def build_huffman_codes(node, current_code="", codes={}):
    if node is None:
        return
    
    if node.char is not None:
        codes[node.char] = current_code
        return
    
    build_huffman_codes(node.left, current_code + "0", codes)
    build_huffman_codes(node.right, current_code + "1", codes)
    
    return codes

def huffman_encoding(text):
    if not text:
        return {}, ""
    
    root = build_huffman_tree(text)
    codes = build_huffman_codes(root)
    
    encoded_text = ''.join([codes[char] for char in text])
    return codes, encoded_text

# Test
text = "hello greedy"
codes, encoded = huffman_encoding(text)
print("Huffman Codes:", codes)
print("Encoded Text:", encoded)