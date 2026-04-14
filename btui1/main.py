import sys
import re
from PyQt6.QtWidgets import *
from uidangkytset import Ui_Dialog  # file bạn convert

# ===== DATA =====
users = []

# ===== CHECK PASSWORD =====
def check_password(pw):
    return (len(pw) >= 8 and
            re.search(r"[a-z]", pw) and
            re.search(r"[A-Z]", pw) and
            re.search(r"[0-9]", pw) and
            re.search(r"[^a-zA-Z0-9]", pw))

# ===== REGISTER WINDOW =====
class Register(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # load ngày tháng năm
        self.ui.cbday.addItems([str(i) for i in range(1, 32)])
        self.ui.cbmonth.addItems([str(i) for i in range(1, 13)])
        self.ui.cbyear.addItems([str(i) for i in range(1990, 2025)])

        # sự kiện nút
        self.ui.pushButton.clicked.connect(self.register)

    def register(self):
        ho = self.ui.txtho.toPlainText()
        ten = self.ui.txtten.toPlainText()
        sdt = self.ui.txtsdtemail.toPlainText()
        mk = self.ui.txtmk.toPlainText()

        # validate
        if not ho or not ten or not sdt or not mk:
            QMessageBox.warning(self, "Lỗi", "Nhập đầy đủ thông tin!")
            return

        if not (self.ui.radioButton.isChecked() or self.ui.radioButton_2.isChecked()):
            QMessageBox.warning(self, "Lỗi", "Chọn giới tính!")
            return

        if not self.ui.checkBox.isChecked():
            QMessageBox.warning(self, "Lỗi", "Phải đồng ý điều khoản!")
            return

        if not check_password(mk):
            QMessageBox.warning(self, "Lỗi", "Mật khẩu yếu!")
            return

        gender = "Nam" if self.ui.radioButton.isChecked() else "Nữ"

        # lưu list
        users.append({
            "ho": ho,
            "ten": ten,
            "sdt": sdt,
            "mk": mk,
            "gender": gender
        })

        QMessageBox.information(self, "OK", "Đăng ký thành công!")

        self.close()
        self.list_window = ListWindow()
        self.list_window.show()

# ===== LIST WINDOW =====
class ListWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Danh sách thành viên")
        self.resize(500, 400)

        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Họ", "Tên", "SĐT", "Mật khẩu", "Giới tính"])

        btn_delete = QPushButton("Xóa")
        btn_edit = QPushButton("Sửa")

        btn_delete.clicked.connect(self.delete_user)
        btn_edit.clicked.connect(self.edit_user)

        layout.addWidget(self.table)
        layout.addWidget(btn_edit)
        layout.addWidget(btn_delete)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        self.table.setRowCount(0)
        for i, user in enumerate(users):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem(user["ho"]))
            self.table.setItem(i, 1, QTableWidgetItem(user["ten"]))
            self.table.setItem(i, 2, QTableWidgetItem(user["sdt"]))
            self.table.setItem(i, 3, QTableWidgetItem(user["mk"]))
            self.table.setItem(i, 4, QTableWidgetItem(user["gender"]))

    def delete_user(self):
        row = self.table.currentRow()
        if row < 0:
            return
        users.pop(row)
        self.load_data()

    def edit_user(self):
        row = self.table.currentRow()
        if row < 0:
            return

        self.edit_window = EditWindow(row)
        self.edit_window.show()

# ===== EDIT WINDOW =====
class EditWindow(Register):
    def __init__(self, index):
        super().__init__()
        self.index = index

        user = users[index]

        self.ui.txtho.setText(user["ho"])
        self.ui.txtten.setText(user["ten"])
        self.ui.txtsdtemail.setText(user["sdt"])
        self.ui.txtmk.setText(user["mk"])

        if user["gender"] == "Nam":
            self.ui.radioButton.setChecked(True)
        else:
            self.ui.radioButton_2.setChecked(True)

    def register(self):
        ho = self.ui.txtho.toPlainText()
        ten = self.ui.txtten.toPlainText()
        sdt = self.ui.txtsdtemail.toPlainText()
        mk = self.ui.txtmk.toPlainText()

        if not ho or not ten or not sdt or not mk:
            QMessageBox.warning(self, "Lỗi", "Nhập đầy đủ thông tin!")
            return

        if not check_password(mk):
            QMessageBox.warning(self, "Lỗi", "Mật khẩu yếu!")
            return

        gender = "Nam" if self.ui.radioButton.isChecked() else "Nữ"

        users[self.index] = {
            "ho": ho,
            "ten": ten,
            "sdt": sdt,
            "mk": mk,
            "gender": gender
        }

        QMessageBox.information(self, "OK", "Cập nhật thành công!")
        self.close()

# ===== RUN =====
app = QApplication(sys.argv)
window = Register()
window.show()
sys.exit(app.exec())