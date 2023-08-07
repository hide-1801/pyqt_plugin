from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QHBoxLayout


class LineEditWithLabel(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

        self.label_title = QLabel(self)
        self.line_edit_context = QLineEdit(self)
        self.root_layout = QHBoxLayout(self)

        self.root_layout.addWidget(self.label_title)
        self.root_layout.addWidget(self.line_edit_context)
        self.setLayout(self.root_layout)

    def setText(self, text: str) -> None:
        self.line_edit_context.setText(text)

    def text(self) -> str:
        return self.line_edit_context.text()

    def setTitle(self, title: str) -> None:
        self.label_title.setText(title)

    def title(self) -> str:
        return self.label_title.text()


class LineEditHideTextWithLabel(LineEditWithLabel):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.line_edit_context.setEchoMode(QLineEdit.EchoMode.Password)
