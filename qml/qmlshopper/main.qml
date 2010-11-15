import Qt 4.7
import Qt.labs.Mx 1.0

Window {
    id: mainwindow
    width: 200
    height: 323

    signal addThing(string thing)

    Entry {
        id: wanted_entry
        hint: "New item"
        y: mainwindow.headerBottom + 10
        anchors.left: parent.left; anchors.right: parent.right
        anchors.margins: 10
        onEnterPressed: addThing(text)
    }

    ListView {
        id: items
        anchors.top: wanted_entry.bottom
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.margins:  10
        model: wantedlist
        delegate: Component { Text { text: display } }
    }
}
