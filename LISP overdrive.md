# Detailed List of Functions and Notations Used

This document provides a comprehensive explanation of every function and notation mentioned during the chat. Each item includes a definition, syntax, examples, and additional notes to help you understand their usage in Common Lisp.

---

## Core Lisp Functions and Constructs

### `defun`

**Definition**: Defines a new function.

**Syntax**:

```lisp
(defun function-name (parameter-list)
  "Optional documentation string."
  function-body)
```

**Example**:

```lisp
(defun add (a b)
  (+ a b))
```

Defines a function `add` that takes two arguments `a` and `b`, and returns their sum.

---

### `let`

**Definition**: Introduces local variables with lexical scope.

**Syntax**:

```lisp
(let ((variable1 value1)
      (variable2 value2)
      ...)
  body)
```

**Example**:

```lisp
(let ((x 10)
      (y 20))
  (+ x y)) ; Returns 30
```

Creates local variables `x` and `y`, then computes their sum.

---

### `reduce`

**Definition**: Reduces a sequence to a single value by applying a binary function cumulatively.

**Syntax**:

```lisp
(reduce function sequence &key :initial-value initial-value)
```

**Example**:

```lisp
(reduce #'+ '(1 2 3 4)) ; Returns 10
```

Sums all elements in the list.

---

### `lambda`

**Definition**: Creates an anonymous function.

**Syntax**:

```lisp
(lambda (parameters)
  body)
```

**Example**:

```lisp
(mapcar (lambda (x) (* x 2)) '(1 2 3)) ; Returns (2 4 6)
```

Doubles each element in the list.

---

### `cond`

**Definition**: Implements conditional branching, similar to a series of if-else statements.

**Syntax**:

```lisp
(cond
  (test1 expression1)
  (test2 expression2)
  ...
  (t default-expression))
```

**Example**:

```lisp
(cond
  ((> x 0) 'positive)
  ((< x 0) 'negative)
  (t 'zero))
```

Returns `'positive`, `'negative`, or `'zero` based on the value of `x`.

---

### `char=`

**Definition**: Checks if two characters are equal.

**Syntax**:

```lisp
(char= char1 char2)
```

**Example**:

```lisp
(char= #\a #\a) ; Returns T (true)
```

Returns true if both characters are the same.

---

### `#\` (Character Notation)

**Definition**: Represents character literals.

**Syntax**:

```lisp
#\character
```

**Examples**:

```lisp
#\a   ; Represents the character 'a'
#\)   ; Represents the character ')'
#\Space ; Represents a space character
```

---

### `cons`

**Definition**: Constructs a new cons cell (pair) from two values, often used to build lists.

**Syntax**:

```lisp
(cons object1 object2)
```

**Example**:

```lisp
(cons 1 '(2 3)) ; Returns (1 2 3)
```

Prepends `1` to the list `(2 3)`.

---

### `if`

**Definition**: Evaluates a test expression and branches accordingly.

**Syntax**:

```lisp
(if test-expression
    then-expression
    else-expression)
```

**Example**:

```lisp
(if (> x 0)
    'positive
    'non-positive)
```

Returns `'positive` if `x` is greater than 0; otherwise, returns `'non-positive`.

---

### `and`

**Definition**: Logical conjunction; returns the first false value or the last true value.

**Syntax**:

```lisp
(and expression1 expression2 ...)
```

**Example**:

```lisp
(and (> x 0) (< x 10)) ; True if x is between 0 and 10
```

Checks if `x` is greater than 0 and less than 10.

---

### `car`

**Definition**: Returns the first element of a list.

**Syntax**:

```lisp
(car list)
```

**Example**:

```lisp
(car '(1 2 3)) ; Returns 1
```

---

### `cdr`

**Definition**: Returns the rest of the list after removing the first element.

**Syntax**:

```lisp
(cdr list)
```

**Example**:

```lisp
(cdr '(1 2 3)) ; Returns (2 3)
```

---

### `return-from`

**Definition**: Exits a named block or function prematurely, returning a specified value.

**Syntax**:

```lisp
(return-from block-name value)
```

**Example**:

```lisp
(defun example ()
  (return-from example 'done))
```

Immediately exits the `example` function, returning `'done`.

---

### `t`

**Definition**: Represents the boolean value true.

**Usage**:

- As a default case in conditionals.
- As a true value in logical expressions.

**Example**:

```lisp
(cond
  ((< x 0) 'negative)
  (t 'non-negative))
```

Uses `t` as the default case.

---

### `null`

**Definition**: Checks if a value is `NIL` (the empty list).

**Syntax**:

```lisp
(null object)
```

**Examples**:

```lisp
(null nil) ; Returns T (true)
(null '(1 2 3)) ; Returns NIL (false)
```

---

### Comments

**Single-line Comment**: Starts with a semicolon `;`.

**Syntax**:

```lisp
; This is a comment
```

**Multi-line Comment**: Enclosed between `#|` and `|#`.

**Syntax**:

```lisp
#|
This is a
multi-line comment.
|#
```

---

### `format`

**Definition**: Produces formatted output.

**Syntax**:

```lisp
(format destination control-string &rest arguments)
```

**Parameters**:

- `destination`: Where to send the output (e.g., `t` for standard output).
- `control-string`: A string that specifies how to format the output.
- `arguments`: Values to be formatted according to the control string.

**Example**:

```lisp
(format t "Hello, ~a!" "world") ; Outputs "Hello, world!"
```

---

### Quoted Lists

**Definition**: Prevents evaluation of a list, treating it as data.

**Syntax**:

```lisp
'(element1 element2 ...)
```

**Example**:

```lisp
'(1 2 3) ; Represents the list (1 2 3)
```

---

### `nthcdr`

**Definition**: Returns the sublist obtained by skipping the first `n` elements.

**Syntax**:

```lisp
(nthcdr n list)
```

**Example**:

```lisp
(nthcdr 2 '(1 2 3 4)) ; Returns (3 4)
```

---

### `subseq`

**Definition**: Extracts a subsequence from a sequence (list or vector).

**Syntax**:

```lisp
(subseq sequence start &optional end)
```

**Parameters**:

- `sequence`: The sequence to extract from.
- `start`: The starting index (inclusive).
- `end`: The ending index (exclusive).

**Example**:

```lisp
(subseq '(a b c d e) 1 4) ; Returns (b c d)
```

---

### `append`

**Definition**: Concatenates lists.

**Syntax**:

```lisp
(append list1 list2 ... listN)
```

**Example**:

```lisp
(append '(1 2) '(3 4)) ; Returns (1 2 3 4)
```

---

### `list`

**Definition**: Creates a list from given elements.

**Syntax**:

```lisp
(list element1 element2 ...)
```

**Example**:

```lisp
(list 1 2 3) ; Returns (1 2 3)
```

---

### `if`

**Definition**: Performs conditional branching.

**Syntax**:

```lisp
(if test
    then-expression
    else-expression)
```

**Example**:

```lisp
(if (evenp x)
    'even
    'odd)
```

Returns `'even` if `x` is even; otherwise, returns `'odd`.

---

### `=`

**Definition**: Checks numerical equality.

**Syntax**:

```lisp
(= number1 number2 ...)
```

**Example**:

```lisp
(= 3 3) ; Returns T (true)
```

---

### `1-` and `1+`

**Definition**:

- `1-`: Decrements a number by one.
- `1+`: Increments a number by one.

**Syntax**:

```lisp
(1- number)
(1+ number)
```

**Examples**:

```lisp
(1- 5) ; Returns 4
(1+ 5) ; Returns 6
```

---

### `setq`

**Definition**: Assigns a value to a variable.

**Syntax**:

```lisp
(setq variable value)
```

**Example**:

```lisp
(setq count 10)
```

Sets the variable `count` to `10`.

---

### `funcall`

**Definition**: Calls a function with specified arguments.

**Syntax**:

```lisp
(funcall function arg1 arg2 ...)
```

**Example**:

```lisp
(defun add (a b) (+ a b))
(funcall #'add 2 3) ; Returns 5
```

Calls the function `add` with arguments `2` and `3`.

---

### `mapcar`

**Definition**: Applies a function to each element of one or more lists.

**Syntax**:

```lisp
(mapcar function list1 &rest more-lists)
```

**Example**:

```lisp
(mapcar #'(lambda (x) (* x x)) '(1 2 3)) ; Returns (1 4 9)
```

Squares each element in the list.

---

### `#'` (Function Designator)

**Definition**: Refers to the function binding of a symbol, ensuring it's treated as a function.

**Syntax**:

```lisp
#'function-name
```

**Example**:

```lisp
(mapcar #'sqrt '(1 4 9)) ; Returns (1.0 2.0 3.0)
```

Applies the `sqrt` function to each element.

**Note**: Using `#'` is similar to using `function`.

---

### Vectors `#()`

**Definition**: Denotes a vector literal.

**Syntax**:

```lisp
#(element1 element2 ...)
```

**Example**:

```lisp
#(1 2 3) ; A vector containing elements 1, 2, and 3
```

---

### Multi-line Comments `#| ... |#`

**Definition**: Encloses comments that span multiple lines.

**Syntax**:

```lisp
#|
This is a
multi-line comment.
|#
```

---

### Read-Time Evaluation `#.`

**Definition**: Evaluates an expression at read-time (when the code is read, before it's compiled or interpreted).

**Syntax**:

```lisp
#.(expression)
```

**Example**:

```lisp
#.(+ 2 3) ; Replaced with 5 at read-time
```

---

## Additional Functions and Concepts

### `nthcdr`

**Definition**: Returns the sublist starting from the nth element.

**Syntax**:

```lisp
(nthcdr n list)
```

**Example**:

```lisp
(nthcdr 2 '(a b c d)) ; Returns (c d)
```

---

### `subseq`

**Definition**: Extracts a subsequence from a sequence.

**Syntax**:

```lisp
(subseq sequence start &optional end)
```

**Example**:

```lisp
(subseq '(a b c d e) 0 3) ; Returns (a b c)
```

---

### `append`

**Definition**: Combines multiple lists into one.

**Syntax**:

```lisp
(append list1 list2 ... listN)
```

**Example**:

```lisp
(append '(a b) '(c d)) ; Returns (a b c d)
```

---

### `1+` and `1-`

**Definition**: Increment or decrement a number by one.

**Syntax**:

```lisp
(1+ number)
(1- number)
```

**Examples**:

```lisp
(1+ 5) ; Returns 6
(1- 5) ; Returns 4
```

---

### `setq`

**Definition**: Assigns a new value to a variable.

**Syntax**:

```lisp
(setq variable value)
```

**Example**:

```lisp
(setq total 100)
```

Sets `total` to `100`.

---

### `funcall`

**Definition**: Calls a function with specified arguments.

**Syntax**:

```lisp
(funcall function-name arg1 arg2 ...)
```

**Example**:

```lisp
(funcall #'+ 1 2 3) ; Returns 6
```

---

### Logical Operators

#### `and`

**Definition**: Returns `NIL` if any argument is `NIL`; otherwise, returns the value of the last argument.

**Syntax**:

```lisp
(and arg1 arg2 ...)
```

**Example**:

```lisp
(and t t) ; Returns T
(and t nil) ; Returns NIL
```

#### `or`

**Definition**: Returns the first non-`NIL` argument; returns `NIL` if all arguments are `NIL`.

**Syntax**:

```lisp
(or arg1 arg2 ...)
```

**Example**:

```lisp
(or nil 'a nil) ; Returns A
```

---

### `not`

**Definition**: Logical negation; returns `T` if the argument is `NIL`, `NIL` otherwise.

**Syntax**:

```lisp
(not expression)
```

**Example**:

```lisp
(not nil) ; Returns T
(not t) ; Returns NIL
```

---

### Function Notation with `#'`

**Definition**: The `#'` reader macro is shorthand for the `function` special operator.

**Syntax**:

```lisp
#'function-name
```

**Example**:

```lisp
(mapcar #'sqrt '(1 4 9)) ; Applies sqrt to each element
```

---

### Character Literals `#\`

**Definition**: Represents a character.

**Syntax**:

```lisp
#\character
```

**Examples**:

```lisp
#\A ; The character 'A'
#\Space ; The space character
```

---

### Read-Time Evaluation `#.`

**Definition**: Evaluates an expression during the read phase.

**Syntax**:

```lisp
#.(expression)
```

**Example**:

```lisp
#.(+ 2 3) ; Replaced with 5 at read-time
```

---

## Usage Examples in Context

### Validating Parentheses Function

```lisp
(defun valid-parentheses (input)
  "Check if the given string of parentheses is valid based on the CFG."
  (let ((stack nil))
    (reduce
     (lambda (acc char)
       (cond
         ((char= char #\() (cons char acc)) ; Push '(' onto stack
         ((char= char #\))
          (if (and acc (char= (car acc) #\())
              (cdr acc) ; Pop from stack
              (return-from valid-parentheses nil))) ; Invalid case
         (t acc))) ; Ignore other characters
     input
     :initial-value stack)
    (null stack))) ; Return T if stack is empty
```

This function checks if a sequence of parentheses is balanced.

---

### Inserting an Element at a Specific Index

```lisp
(defun insert-at-index (lst element index)
  "Inserts ELEMENT into LST at the specified INDEX."
  (let ((prefix (subseq lst 0 index))
        (suffix (nthcdr index lst)))
    (append prefix (list element) suffix)))
```

Inserts `element` into `lst` at position `index`.

---

### Example of Using `subseq`

```lisp
(subseq lst 0 (1+ index))
```

Extracts elements from the start of `lst` up to and including `index`.

---

## Conclusion

This detailed list covers all functions and notations used during the chat, providing definitions, syntax, examples, and explanations to help you understand their usage in Common Lisp. Whether you're new to Lisp or brushing up on specific functions, this guide serves as a comprehensive reference.



# Comparison Functions in Common Lisp

In Common Lisp, values can be compared using various functions tailored to specific data types and purposes. Below is a detailed overview, formatted in Markdown.

---

## 1. Equality Operators

### = — Numerical Equality

- Used to compare numbers.
- Returns `T` if all arguments are numerically equal, `NIL` otherwise.

**Syntax**:

```lisp
(= num1 num2 ...)
```

**Examples**:

```lisp
(= 5 5)          ; T
(= 5 5 5)        ; T
(= 5 3)          ; NIL
(= 5 5.0)        ; T (handles type promotion)
```

---

### `eql` — General Equality

- Tests for equality of:
    - Numbers of the same type and value.
    - Symbols (by identity).
    - Characters (case-sensitive).

**Syntax**:

```lisp
(eql obj1 obj2)
```

**Examples**:

```lisp
(eql 42 42)      ; T
(eql 42 42.0)    ; NIL (integer vs float)
(eql 'foo 'foo)  ; T (same symbol)
(eql #\A #\a)    ; NIL (case-sensitive)
```

---

### `equal` — Structural Equality

- Compares:
    - Lists, arrays, and strings element by element.
    - Symbols and numbers like `eql`.

**Syntax**:

```lisp
(equal obj1 obj2)
```

**Examples**:

```lisp
(equal '(1 2 3) '(1 2 3)) ; T
(equal "abc" "abc")       ; T
(equal 42 42)             ; T
(equal 42 42.0)           ; NIL (different types)
```

---

### `equalp` — Case-Insensitive and Generalized Equality

- Like `equal`, but:
    - Ignores case for strings and characters.
    - Compares numbers across types (e.g., `42` vs `42.0`).

**Syntax**:

```lisp
(equalp obj1 obj2)
```

**Examples**:

```lisp
(equalp '(1 2 3) '(1 2 3)) ; T
(equalp "abc" "ABC")       ; T
(equalp 42 42.0)           ; T
```

---

## 2. Relational Operators for Numbers

### `<`, `<=`, `>`, `>=` — Numerical Comparisons

- Compare numbers for order.

**Syntax**:

```lisp
(< num1 num2 ...)
(<= num1 num2 ...)
(> num1 num2 ...)
(>= num1 num2 ...)
```

**Examples**:

```lisp
(< 3 5)          ; T
(> 5 3)          ; T
(<= 5 5)         ; T
(< 3 3)          ; NIL
(> 3 5 2)        ; NIL (fails when 5 > 2 is false)
```

---

## 3. String Comparisons

### `string=`, `string<`, `string>`, `string<=`, `string>=`

- Case-sensitive string comparisons.

**Syntax**:

```lisp
(string= string1 string2)
(string< string1 string2)
(string> string1 string2)
(string<= string1 string2)
(string>= string1 string2)
```

**Examples**:

```lisp
(string= "abc" "abc")      ; T
(string< "abc" "def")      ; T ("abc" comes before "def")
(string> "abc" "ABC")      ; T (case-sensitive)
```

---

### `string-equal`, `string-lessp`, `string-greaterp`, etc.

- Case-insensitive string comparisons.

**Examples**:

```lisp
(string-equal "abc" "ABC") ; T
(string-lessp "abc" "DEF") ; T
```

---

## 4. Character Comparisons

### `char=`, `char<`, `char>`, `char<=`, `char>=`

- Compares characters for equality or order.

**Syntax**:

```lisp
(char= char1 char2)
(char< char1 char2)
```

**Examples**:

```lisp
(char= #\a #\a)  ; T
(char< #\a #\z)  ; T
(char> #\A #\a)  ; NIL (case-sensitive)
```

---

### `char-equal`, `char-lessp`, etc.

- Case-insensitive character comparisons.

**Examples**:

```lisp
(char-equal #\A #\a) ; T
(char-lessp #\a #\Z) ; T
```

---

## 5. List Comparisons

Use `equal` or `equalp` for structural equality of lists.

**Examples**:

```lisp
(equal '(1 2 3) '(1 2 3))   ; T
(equalp '(1 2 3) '(1 2 3))  ; T
(equal '(1 2 3) '(1 2 3.0)) ; NIL (exact equality fails)
(equalp '(1 2 3) '(1 2 3.0)); T (generalized equality)
```

---

## 6. Custom Comparisons with `funcall`

You can dynamically call a comparison function using `funcall` or `apply`.

**Examples**:

```lisp
(funcall #'= 42 42)         ; T
(funcall #'string< "a" "b") ; T
```

---

## Summary Table of Comparison Functions

|**Function**|**Purpose**|
|---|---|
|`=`|Numerical equality.|
|`eql`|Symbol/number/character equality.|
|`equal`|Structural equality for lists, strings, arrays.|
|`equalp`|Case-insensitive and generalized equality.|
|`<`, `<=`, `>`, `>=`|Relational comparisons for numbers.|
|`string=`, `string<`, etc.|Case-sensitive string comparisons.|
|`string-equal`, etc.|Case-insensitive string comparisons.|
|`char=`, `char<`, etc.|Character comparisons (case-sensitive).|
|`char-equal`, etc.|Character comparisons (case-insensitive).|

---

# String formatting

| **Directive** | **Purpose**                                                            | **Example**                                 |
| ------------- | ---------------------------------------------------------------------- | ------------------------------------------- |
| `~a`          | Inserts a string (any type is converted).                              | `~a` for "Hello".                           |
| `~s`          | Inserts a string (Lisp-readable form).                                 | `~s` for `"Hello"`.                         |
| `~d`          | Inserts a decimal integer.                                             | `~d` for `42`.                              |
| `~f`          | Inserts a floating-point number.                                       | `~f` for `3.14`.                            |
| `~%`          | Inserts a newline.                                                     | `~%`.                                       |
| `~&`          | Inserts a fresh line if the previous output didn’t end with a newline. | `~&`.                                       |
| `~t`          | Inserts horizontal tabulation.                                         | `~10t` aligns to column 10.                 |
| `~&`          | Ensures fresh line; no extra newline.                                  | `~&`.                                       |
| `~A`          | General-purpose printing. Converts and embeds any type.                | `~A` for "Hello" → `"Hello"`                |
| `~S`          | Prints with quoting if needed (useful for Lisp objects).               | `~S` for "Hello" → `"\"Hello\""`            |
| `~D`          | Decimal integer (base 10).                                             | `~D` for `42` → `"42"`                      |
| `~%`          | Inserts a newline.                                                     | `"Line 1~%Line 2"` → `Line 1`  <br>`Line 2` |
| `~F`          | Fixed-point floating number.                                           | `~F` for `3.14159` → `"3.141590"`           |
| `~E`          | Exponential notation.                                                  | `~E` for `31415.92` → `"3.141592E+4"`       |
| `~G`          | Flexible floating-point format (chooses `~F` or `~E`).                 | `~G` for `31415.92` → `"31415.92"`          |
| `~C`          | Character.                                                             | `~C` for `#\A` → `"A"`                      |
| `~X`          | Hexadecimal integer (base 16).                                         | `~X` for `255` → `"FF"`                     |
| `~O`          | Octal integer (base 8).                                                | `~O` for `10` → `"12"`                      |
| `~B`          | Binary integer (base 2).                                               | `~B` for `10` → `"1010"`                    |
The **`format`** function in Common Lisp is similar to `printf` in C, but it is more powerful and flexible. It uses a **control string** with **directives** (special sequences starting with `~`) to format text, numbers, and other data types. Here’s a detailed breakdown:

The **`format`** function in Common Lisp is similar to `printf` in C, but it is more powerful and flexible. It uses a **control string** with **directives** (special sequences starting with `~`) to format text, numbers, and other data types. Here’s a detailed breakdown:

---
## **Examples**

### 1. **Embedding Integers and Strings**

```lisp
(format t "Hello, ~A! You have ~D unread messages.~%" "Alice" 42)
;; Output:
;; Hello, Alice! You have 42 unread messages.
;; Returns: NIL
```

Explanation:

- `~A`: Embeds the string `"Alice"`.
- `~D`: Embeds the integer `42`.
- `~%`: Inserts a newline.

---

### 2. **Returning a Formatted String**

```lisp
(format nil "Pi is approximately ~F." 3.14159)
;; Returns:
;; "Pi is approximately 3.141590."
```

Here:

- `~F`: Formats the floating-point number `3.14159` with fixed-point notation.

---

### 3. **Newlines with `~%`**

```lisp
(format t "Line 1~%Line 2~%Line 3")
;; Output:
;; Line 1
;; Line 2
;; Line 3
```

---

### 4. **Hexadecimal, Octal, and Binary**

```lisp
(format t "Hex: ~X, Octal: ~O, Binary: ~B~%" 255 255 255)
;; Output:
;; Hex: FF, Octal: 377, Binary: 11111111
```

Here:

- `~X`: Converts `255` to hexadecimal.
- `~O`: Converts `255` to octal.
- `~B`: Converts `255` to binary.

---

### 5. **Aligning and Padding**

You can control field width and alignment with numbers in the directive.

#### Example: Right-Aligned Integers

```lisp
(format t "Right-aligned: |~5D|~%" 42)
;; Output:
;; Right-aligned: |   42|
```

Here:

- `~5D`: Formats the integer `42` in a field of width 5, right-aligned.

#### Example: Left-Aligned Integers

```lisp
(format t "Left-aligned: |~-5D|~%" 42)
;; Output:
;; Left-aligned: |42   |
```

Here:

- `~-5D`: The `-` ensures left alignment.

---

### 6. **Working with Multiple Lines**

```lisp
(format t "Name: ~A~%Age: ~D~%Location: ~A~%" "Alice" 30 "Wonderland")
;; Output:
;; Name: Alice
;; Age: 30
;; Location: Wonderland
```

---

## **Comparison to `printf` in C**

|**Aspect**|**Common Lisp `format`**|**C `printf`**|
|---|---|---|
|**Syntax**|Prefix notation: `(format ...)`.|Infix-style: `printf(...)`.|
|**Newline**|Explicit: `~%`.|Implicit: `\n`.|
|**Directives**|Prefixed by `~` (e.g., `~A`, `~D`).|`%` for directives (e.g., `%d`, `%s`).|
|**Flexibility**|More powerful and extensible (e.g., `~A` works for any type).|Limited to predefined types.|
|**Streams**|Works with any output stream or string.|Primarily stdout or file streams.|

---

## **Advanced Usage**

### Combining Formatting Features

```lisp
(format t "~A is ~D years old and has a GPA of ~5,2F.~%" "Bob" 21 3.75)
;; Output:
;; Bob is 21 years old and has a GPA of  3.75.
```

Here:

- `~A`: Embeds the string `"Bob"`.
- `~D`: Embeds the integer `21`.
- `~5,2F`: Formats `3.75` as a floating-point number in a field width of 5, with 2 decimal places.

---

### Summary of `format`

1. **Core Idea**:
    
    - `format` combines a control string (like a template) with arguments to generate formatted output.
2. **Usage**:
    
    - Print directly to the console with `t`.
    - Return formatted strings with `nil`.
3. **Directives**:
    
    - Use `~A`, `~D`, `~F`, etc., to embed values of various types.
4. **Similarities to C’s `printf`**:
    
    - Conceptually similar, but Lisp's `format` is more powerful and flexible.

Let me know if you’d like more examples or have specific use cases! 😊