1. Числа Фибоначчи


import java.util.ArrayList;
import java.util.List;

public class Fibonacci {
    
    // Рекурсивное вычисление чисел Фибоначчи
    public static long fibonacciRecursive(int n) {
        if (n <= 1) return n;
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
    }
    
    // Итеративное вычисление чисел Фибоначчи
    public static long fibonacciIterative(int n) {
        if (n <= 1) return n;
        
        long a = 0, b = 1, c;
        for (int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
    
    // Генерация последовательности Фибоначчи
    public static List<Long> fibonacciSequence(int n) {
        List<Long> sequence = new ArrayList<>();
        if (n >= 1) sequence.add(0L);
        if (n >= 2) sequence.add(1L);
        
        for (int i = 2; i < n; i++) {
            sequence.add(sequence.get(i - 1) + sequence.get(i - 2));
        }
        return sequence;
    }
    
    public static void main(String[] args) {
        System.out.println("Fibonacci Recursive(10): " + fibonacciRecursive(10));
        System.out.println("Fibonacci Iterative(10): " + fibonacciIterative(10));
        
        List<Long> seq = fibonacciSequence(10);
        System.out.println("Fibonacci Sequence(10): " + seq);
    }
}


2. Бинарная куча


import java.util.ArrayList;
import java.util.List;

public class BinaryHeap {
    private List<Integer> heap;
    
    public BinaryHeap() {
        heap = new ArrayList<>();
    }
    
    private int parent(int i) {
        return (i - 1) / 2;
    }
    
    private int leftChild(int i) {
        return 2 * i + 1;
    }
    
    private int rightChild(int i) {
        return 2 * i + 2;
    }
    
    private void heapifyUp(int i) {
        while (i > 0 && heap.get(i) < heap.get(parent(i))) {
            swap(i, parent(i));
            i = parent(i);
        }
    }
    
    private void heapifyDown(int i) {
        int minIndex = i;
        int left = leftChild(i);
        int right = rightChild(i);
        
        if (left < heap.size() && heap.get(left) < heap.get(minIndex)) {
            minIndex = left;
        }
        
        if (right < heap.size() && heap.get(right) < heap.get(minIndex)) {
            minIndex = right;
        }
        
        if (i != minIndex) {
            swap(i, minIndex);
            heapifyDown(minIndex);
        }
    }
    
    private void swap(int i, int j) {
        int temp = heap.get(i);
        heap.set(i, heap.get(j));
        heap.set(j, temp);
    }
    
    public void push(int value) {
        heap.add(value);
        heapifyUp(heap.size() - 1);
    }
    
    public int pop() {
        if (heap.isEmpty()) {
            throw new IllegalStateException("Heap is empty");
        }
        
        int minValue = heap.get(0);
        heap.set(0, heap.get(heap.size() - 1));
        heap.remove(heap.size() - 1);
        
        if (!heap.isEmpty()) {
            heapifyDown(0);
        }
        
        return minValue;
    }
    
    public int peek() {
        if (heap.isEmpty()) {
            throw new IllegalStateException("Heap is empty");
        }
        return heap.get(0);
    }
    
    public boolean isEmpty() {
        return heap.isEmpty();
    }
    
    public int size() {
        return heap.size();
    }
    
    public void display() {
        System.out.println("Heap: " + heap);
    }
    
    public static void main(String[] args) {
        BinaryHeap heap = new BinaryHeap();
        int[] numbers = {5, 3, 8, 1, 2, 7};
        
        for (int num : numbers) {
            heap.push(num);
        }
        
        System.out.println("Binary Heap operations:");
        heap.display();
        System.out.println("Min element: " + heap.peek());
        
        System.out.print("Elements in order: ");
        while (!heap.isEmpty()) {
            System.out.print(heap.pop() + " ");
        }
        System.out.println();
    }
}



3. Хеш-таблица


import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class HashTable<K, V> {
    private static class KeyValue<K, V> {
        K key;
        V value;
        
        KeyValue(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }
    
    private List<LinkedList<KeyValue<K, V>>> table;
    private int capacity;
    private int size;
    
    public HashTable(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.table = new ArrayList<>(capacity);
        
        for (int i = 0; i < capacity; i++) {
            table.add(new LinkedList<>());
        }
    }
    
    public HashTable() {
        this(10);
    }
    
    private int hash(K key) {
        return Math.abs(key.hashCode()) % capacity;
    }
    
    public void put(K key, V value) {
        int index = hash(key);
        LinkedList<KeyValue<K, V>> bucket = table.get(index);
        
        // Проверка на существование ключа
        for (KeyValue<K, V> kv : bucket) {
            if (kv.key.equals(key)) {
                kv.value = value;
                return;
            }
        }
        
        // Добавление новой пары
        bucket.add(new KeyValue<>(key, value));
        size++;
    }
    
    public V get(K key) {
        int index = hash(key);
        LinkedList<KeyValue<K, V>> bucket = table.get(index);
        
        for (KeyValue<K, V> kv : bucket) {
            if (kv.key.equals(key)) {
                return kv.value;
            }
        }
        
        throw new IllegalArgumentException("Key not found: " + key);
    }
    
    public void remove(K key) {
        int index = hash(key);
        LinkedList<KeyValue<K, V>> bucket = table.get(index);
        
        for (KeyValue<K, V> kv : bucket) {
            if (kv.key.equals(key)) {
                bucket.remove(kv);
                size--;
                return;
            }
        }
        
        throw new IllegalArgumentException("Key not found: " + key);
    }
    
    public boolean contains(K key) {
        try {
            get(key);
            return true;
        } catch (IllegalArgumentException e) {
            return false;
        }
    }
    
    public int size() {
        return size;
    }
    
    public void display() {
        for (int i = 0; i < capacity; i++) {
            System.out.print("Bucket " + i + ": ");
            LinkedList<KeyValue<K, V>> bucket = table.get(i);
            for (KeyValue<K, V> kv : bucket) {
                System.out.print("[" + kv.key + ": " + kv.value + "] ");
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args) {
        HashTable<String, Integer> ht = new HashTable<>();
        
        // Добавление элементов
        ht.put("apple", 10);
        ht.put("banana", 20);
        ht.put("orange", 30);
        ht.put("apple", 15);  // Обновление значения
        
        System.out.println("Hash Table contents:");
        ht.display();
        
        System.out.println("\nGet operations:");
        System.out.println("apple: " + ht.get("apple"));
        System.out.println("banana: " + ht.get("banana"));
        
        // Проверка наличия ключа
        System.out.println("\nContains check:");
        System.out.println("orange in table: " + ht.contains("orange"));
        System.out.println("grape in table: " + ht.contains("grape"));
        
        // Удаление элемента
        ht.remove("banana");
        System.out.println("\nAfter removing banana:");
        ht.display();
    }
}
