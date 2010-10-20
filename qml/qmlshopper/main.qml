import Qt 4.7
import Qt.labs.Mx 1.0

Window {
    id: mainwindow
    width: 200
    height: 323

    Entry {
        id: wanted_entry
        hint: "New item"
        y: mainwindow.headerBottom + 10
        anchors.left: parent.left; anchors.right: parent.right
        anchors.margins: 10
    }

    Button {
        id: somebutton
        text: "moro"
        anchors.centerIn: parent
    }
}
