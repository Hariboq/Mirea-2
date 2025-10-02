1. Числа Фибоначчи


#include <iostream>
#include <vector>

using namespace std;

// Рекурсивное вычисление чисел Фибоначчи
long long fibonacciRecursive(int n) {
    if (n <= 1) return n;
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2);
}

// Итеративное вычисление чисел Фибоначчи
long long fibonacciIterative(int n) {
    if (n <= 1) return n;
    
    long long a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

// Генерация последовательности Фибоначчи
vector<long long> fibonacciSequence(int n) {
    vector<long long> sequence;
    if (n >= 1) sequence.push_back(0);
    if (n >= 2) sequence.push_back(1);
    
    for (int i = 2; i < n; i++) {
        sequence.push_back(sequence[i-1] + sequence[i-2]);
    }
    return sequence;
}

int main() {
    cout << "Fibonacci Recursive(10): " << fibonacciRecursive(10) << endl;
    cout << "Fibonacci Iterative(10): " << fibonacciIterative(10) << endl;
    
    vector<long long> seq = fibonacciSequence(10);
    cout << "Fibonacci Sequence(10): ";
    for (long long num : seq) {
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}



2. Бинарная куча



#include <iostream>
#include <vector>
#include <algorithm>
#include <stdexcept>

using namespace std;

class BinaryHeap {
private:
    vector<int> heap;
    
    int parent(int i) { return (i - 1) / 2; }
    int leftChild(int i) { return 2 * i + 1; }
    int rightChild(int i) { return 2 * i + 2; }
    
    void heapifyUp(int i) {
        while (i > 0 && heap[i] < heap[parent(i)]) {
            swap(heap[i], heap[parent(i)]);
            i = parent(i);
        }
    }
    
    void heapifyDown(int i) {
        int minIndex = i;
        int left = leftChild(i);
        int right = rightChild(i);
        
        if (left < heap.size() && heap[left] < heap[minIndex]) {
            minIndex = left;
        }
        
        if (right < heap.size() && heap[right] < heap[minIndex]) {
            minIndex = right;
        }
        
        if (i != minIndex) {
            swap(heap[i], heap[minIndex]);
            heapifyDown(minIndex);
        }
    }
    
public:
    void push(int value) {
        heap.push_back(value);
        heapifyUp(heap.size() - 1);
    }
    
    int pop() {
        if (heap.empty()) {
            throw runtime_error("Heap is empty");
        }
        
        int minValue = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        
        if (!heap.empty()) {
            heapifyDown(0);
        }
        
        return minValue;
    }
    
    int peek() {
        if (heap.empty()) {
            throw runtime_error("Heap is empty");
        }
        return heap[0];
    }
    
    bool empty() {
        return heap.empty();
    }
    
    size_t size() {
        return heap.size();
    }
    
    void display() {
        cout << "Heap: ";
        for (int value : heap) {
            cout << value << " ";
        }
        cout << endl;
    }
};

int main() {
    BinaryHeap heap;
    vector<int> numbers = {5, 3, 8, 1, 2, 7};
    
    for (int num : numbers) {
        heap.push(num);
    }
    
    cout << "Binary Heap operations:" << endl;
    heap.display();
    cout << "Min element: " << heap.peek() << endl;
    
    cout << "Elements in order: ";
    while (!heap.empty()) {
        cout << heap.pop() << " ";
    }
    cout << endl;
    
    return 0;
}



3. Хеш-таблица


#include <iostream>
#include <vector>
#include <list>
#include <functional>

using namespace std;

template<typename K, typename V>
class HashTable {
private:
    struct KeyValue {
        K key;
        V value;
        KeyValue(const K& k, const V& v) : key(k), value(v) {}
    };
    
    vector<list<KeyValue>> table;
    size_t capacity;
    size_t size;
    
    size_t hash(const K& key) {
        return hash<K>{}(key) % capacity;
    }
    
public:
    HashTable(size_t cap = 10) : capacity(cap), size(0) {
        table.resize(capacity);
    }
    
    void put(const K& key, const V& value) {
        size_t index = hash(key);
        auto& bucket = table[index];
        
        // Проверка на существование ключа
        for (auto& kv : bucket) {
            if (kv.key == key) {
                kv.value = value;
                return;
            }
        }
        
        // Добавление новой пары
        bucket.emplace_back(key, value);
        size++;
    }
    
    V get(const K& key) {
        size_t index = hash(key);
        auto& bucket = table[index];
        
        for (const auto& kv : bucket) {
            if (kv.key == key) {
                return kv.value;
            }
        }
        
        throw runtime_error("Key not found");
    }
    
    void remove(const K& key) {
        size_t index = hash(key);
        auto& bucket = table[index];
        
        for (auto it = bucket.begin(); it != bucket.end(); ++it) {
            if (it->key == key) {
                bucket.erase(it);
                size--;
                return;
            }
        }
        
        throw runtime_error("Key not found");
    }
    
    bool contains(const K& key) {
        try {
            get(key);
            return true;
        } catch (const runtime_error&) {
            return false;
        }
    }
    
    size_t getSize() const {
        return size;
    }
    
    void display() {
        for (size_t i = 0; i < capacity; i++) {
            cout << "Bucket " << i << ": ";
            for (const auto& kv : table[i]) {
                cout << "[" << kv.key << ": " << kv.value << "] ";
            }
            cout << endl;
        }
    }
};

int main() {
    HashTable<string, int> ht;
    
    // Добавление элементов
    ht.put("apple", 10);
    ht.put("banana", 20);
    ht.put("orange", 30);
    ht.put("apple", 15);  // Обновление значения
    
    cout << "Hash Table contents:" << endl;
    ht.display();
    
    cout << "\nGet operations:" << endl;
    cout << "apple: " << ht.get("apple") << endl;
    cout << "banana: " << ht.get("banana") << endl;
    
    // Проверка наличия ключа
    cout << "\nContains check:" << endl;
    cout << "orange in table: " << (ht.contains("orange") ? "true" : "false") << endl;
    cout << "grape in table: " << (ht.contains("grape") ? "true" : "false") << endl;
    
    // Удаление элемента
    ht.remove("banana");
    cout << "\nAfter removing banana:" << endl;
    ht.display();
    
    return 0;
}

