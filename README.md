

```md
# Quiz Game

This is a Python-based quiz game that allows an admin to create and manage a list of quiz questions by category, and students to participate in the quiz by selecting categories and answering the questions. It features functionalities for adding, deleting, and modifying quiz questions, as well as displaying student results in a bar chart.

## Features

- **Admin Panel**: 
  - Add, delete, and modify quiz questions by category.
- **Student Registration**: 
  - Multiple students can register to play.
- **Quiz Game**: 
  - Students can select a category and answer quiz questions.
- **Results Display**: 
  - Shows student scores in a bar chart using `matplotlib`.
  
## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/quiz-game.git
    ```

2. Navigate to the project directory:
    ```bash
    cd quiz-game
    ```

3. Install the required Python packages:
    ```bash
    pip install numpy pandas matplotlib
    ```

## How to Run

1. Run the script:
    ```bash
    python quiz_game.py
    ```

2. Choose from the following options in the menu:
    - **1. Admin Login**: 
      - Default username: `Admin`
      - Default password: `admin123`
    - **2. Register Student**: 
      - Register students who want to play the quiz.
    - **3. Play Quiz**: 
      - Students can choose categories and answer quiz questions.
    - **4. Show Results**: 
      - Displays a bar chart of student scores.
    - **5. Exit**: 
      - Exits the program.

## Admin Functions

- **Add Question**: Add a question and its answer to a specific category.
- **Delete Question/Category**: Remove a question or an entire category.
- **Modify Question**: Update a question and its answer within a category.

## Example

1. **Admin adds a question**:
    - Category: "Math"
    - Question: "What is 2+2?"
    - Answer: "4"

2. **Student plays the quiz**:
    - Selects category "Math"
    - Question: "What is 2+2?"
    - Student answers: "4" (Correct)

3. **Results Display**:
    - Shows a bar chart of all student scores.

## Libraries Used

- `numpy`: For numerical operations.
- `pandas`: For handling student data and creating a DataFrame for scores.
- `matplotlib`: For plotting a bar chart of student scores.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

