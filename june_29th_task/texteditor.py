from stack_class import Stack
class TextEditor:

    def __init__(self):

        self.content = ""

        self._undo_stack = Stack()

    def _save_state(self):

        self._undo_stack.push(self.content)

    def type_text(self, text):

        self._save_state()

        self.content += text

    def undo(self):

        if not self._undo_stack.is_empty():

            self.content = self._undo_stack.pop()


editor = TextEditor()

editor.type_text("Hello")
editor.type_text(" World")

editor.undo()

print(editor.content)