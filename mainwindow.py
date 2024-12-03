# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowTKcJjU.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import (
    QAction,
    QFont,
    QIcon,
    QPixmap,
    QStandardItemModel,
    QStandardItem,
    QDesktopServices,
)
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMenu,
    QMenuBar,
    QPlainTextEdit,
    QStatusBar,
    QTabWidget,
    QTableView,
    QWidget,
    QFileDialog,
    QDialog,
    QLabel,
    QMessageBox,
)

# my code begin
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import setup
import io

OMP_NUM_THREADS = 1

# my code end


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        icon = QIcon()
        icon.addFile("dat-logo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionOpenDATFile = QAction(MainWindow)
        self.actionOpenDATFile.setObjectName("actionOpenDATFile")
        icon1 = QIcon(QIcon.fromTheme("document-open"))
        self.actionOpenDATFile.setIcon(icon1)
        self.actionSetup = QAction(MainWindow)
        self.actionSetup.setObjectName("actionSetup")
        icon2 = QIcon(QIcon.fromTheme("document-properties"))
        self.actionSetup.setIcon(icon2)
        self.actionRun = QAction(MainWindow)
        self.actionRun.setObjectName("actionRun")
        icon3 = QIcon(QIcon.fromTheme("media-playback-start"))
        self.actionRun.setIcon(icon3)
        self.actionGithubProject = QAction(MainWindow)
        self.actionGithubProject.setObjectName("actionGithubProject")
        icon4 = QIcon(QIcon.fromTheme("emblem-favorite"))
        self.actionGithubProject.setIcon(icon4)
        self.actionSaveReport = QAction(MainWindow)
        self.actionSaveReport.setObjectName("actionSaveReport")
        icon5 = QIcon(QIcon.fromTheme("document-save"))
        self.actionSaveReport.setIcon(icon5)
        self.actionSaveGraph = QAction(MainWindow)
        self.actionSaveGraph.setObjectName("actionSaveGraph")
        self.actionSaveGraph.setIcon(icon5)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        icon6 = QIcon(QIcon.fromTheme("application-exit"))
        self.actionExit.setIcon(icon6)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.tabInput = QWidget()
        self.tabInput.setObjectName("tabInput")
        self.gridLayout_2 = QGridLayout(self.tabInput)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableView = QTableView(self.tabInput)
        self.tableView.setObjectName("tableView")
        font = QFont()
        font.setPointSize(11)
        self.tableView.setFont(font)

        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabInput, "")
        self.tabReport = QWidget()
        self.tabReport.setObjectName("tabReport")
        self.gridLayout_3 = QGridLayout(self.tabReport)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.plainTextEdit = QPlainTextEdit(self.tabReport)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setOverwriteMode(True)

        self.gridLayout_3.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabReport, "")
        self.tabGraph = QWidget()
        self.tabGraph.setObjectName("tabGraph")
        self.gridLayout_4 = QGridLayout(self.tabGraph)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QLabel(self.tabGraph)
        self.label.setObjectName("label")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabGraph, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuCluster = QMenu(self.menubar)
        self.menuCluster.setObjectName("menuCluster")
        self.menuAnalyze = QMenu(self.menubar)
        self.menuAnalyze.setObjectName("menuAnalyze")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.tabWidget, self.tableView)
        QWidget.setTabOrder(self.tableView, self.plainTextEdit)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCluster.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpenDATFile)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSaveReport)
        self.menuFile.addAction(self.actionSaveGraph)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuCluster.addAction(self.actionSetup)
        self.menuAnalyze.addAction(self.actionRun)
        self.menuHelp.addAction(self.actionGithubProject)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        # my code begin
        self.cluster_number = 1
        self.cluster_method = "K-Means"

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Name", "Attr", "E", "N", "U"])
        self.tableView.setModel(self.model)

        self.actionOpenDATFile.triggered.connect(self.on_actionOpenDATFile_triggered)
        self.actionSaveReport.triggered.connect(self.on_actionSaveReport_triggered)
        self.actionSaveGraph.triggered.connect(self.on_actionSaveGraph_triggered)
        self.actionExit.triggered.connect(QApplication.instance().quit)
        self.actionSetup.triggered.connect(self.on_actionSetup_triggered)
        self.actionRun.triggered.connect(self.on_actionRun_triggered)
        self.actionGithubProject.triggered.connect(
            self.on_actionGithubProject_triggered
        )
        # my code end

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "DAT Analysis Tool V1.0", None)
        )
        self.actionOpenDATFile.setText(
            QCoreApplication.translate("MainWindow", "Open DAT File", None)
        )
        self.actionSetup.setText(
            QCoreApplication.translate("MainWindow", "Setup", None)
        )
        self.actionRun.setText(QCoreApplication.translate("MainWindow", "Run", None))
        self.actionGithubProject.setText(
            QCoreApplication.translate("MainWindow", "Github Project", None)
        )
        self.actionSaveReport.setText(
            QCoreApplication.translate("MainWindow", "Save Report", None)
        )
        self.actionSaveGraph.setText(
            QCoreApplication.translate("MainWindow", "Save Graph", None)
        )
        self.actionExit.setText(QCoreApplication.translate("MainWindow", "Exit", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabInput),
            QCoreApplication.translate("MainWindow", "Input", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabReport),
            QCoreApplication.translate("MainWindow", "Report", None),
        )
        self.label.setText("")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabGraph),
            QCoreApplication.translate("MainWindow", "Graph", None),
        )
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menuCluster.setTitle(
            QCoreApplication.translate("MainWindow", "Cluster", None)
        )
        self.menuAnalyze.setTitle(
            QCoreApplication.translate("MainWindow", "Analyze", None)
        )
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "About", None))

    # retranslateUi

    # my code begin
    def on_actionOpenDATFile_triggered(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["Name", "Attr", "E", "N", "U"])
        self.cluster_source, _ = QFileDialog.getOpenFileName(
            None, "Open DAT File", "", "DAT Files (*.dat)", ""
        )
        with open(self.cluster_source, "r") as fr:
            self.dataset = []
            for line in fr:
                items = line.strip().split(",")
                self.model.appendRow([QStandardItem(item) for item in items])
                self.dataset.append([float(item) for item in items[-3:]])

    def on_actionSaveReport_triggered(self):
        fpath, _ = QFileDialog.getSaveFileName(
            None, "Save Report File", "", "Report Files (*.txt)", ""
        )
        with open(fpath, "w") as fw:
            fw.write(self.plainTextEdit.toPlainText())

    def on_actionSaveGraph_triggered(self):
        fpath, _ = QFileDialog.getSaveFileName(
            None, "Save Graph File", "", "Graph Files (*.png)", ""
        )
        self.tabGraph.grab().save(fpath)

    def on_actionSetup_triggered(self):
        dialog = QDialog()
        ui = setup.Ui_Dialog()
        ui.setupUi(dialog)
        dialog.exec_()
        self.cluster_number = ui.spinBox.value()
        self.cluster_method = ui.comboBox.currentText()

    def on_actionRun_triggered(self):
        self.statusbar.showMessage("Running...")
        try:
            # Cluster
            match self.cluster_method:
                case "K-Means":
                    kmeans = KMeans(n_clusters=self.cluster_number)
                    kmeans.fit(self.dataset)
                    self.labels = kmeans.labels_
                    self.centroids = kmeans.cluster_centers_
            # Report
            self.h_stds, self.v_stds = [], []
            for lab in range(self.cluster_number):
                es, ns, us = [], [], []
                for i in range(len(self.dataset)):
                    if lab == self.labels[i]:
                        es.append(self.dataset[i][0])
                        ns.append(self.dataset[i][1])
                        us.append(self.dataset[i][2])
                e_std, n_std, u_std = np.std(es), np.std(ns), np.std(us)
                self.h_stds.append(np.sqrt(e_std**2 + n_std**2))
                self.v_stds.append(u_std)
            report = "-------- Settings --------\n"
            report += f"Cluster Source: {self.cluster_source}\n"
            report += f"Cluster Method: {self.cluster_method}\n"
            report += f"Cluster Number: {self.cluster_number}\n\n"
            report += "-------- Results --------\n"
            report += "Cluster Labels:\n"
            for i in self.labels:
                report += f"{i} "
            report += "\n\nCluster Centroids:\n"
            for i, c in enumerate(self.centroids):
                report += f"{i:2d} | {c[0]:.3f} | {c[1]:.3f} | {c[2]:.3f}\n"
            report += f"\nHorizontal STDs:\n"
            for i, h_std in enumerate(self.h_stds):
                report += f"{i:2d} | {h_std:.6f}\n"
            report += f"\nVertical STDs:\n"
            for i, v_std in enumerate(self.v_stds):
                report += f"{i:2d} | {v_std:.6f}\n"
            self.plainTextEdit.setPlainText(report)
            # Plot
            plt.figure(figsize=(5, 3))
            plt.xlabel("E")
            plt.ylabel("N", rotation=0, loc="top")
            plt.scatter(
                [e for e, _, _ in self.dataset],
                [n for _, n, _ in self.dataset],
                c=self.labels,
                cmap="cool",
            )
            plt.scatter(
                [e for e, _, _ in self.centroids],
                [n for _, n, _ in self.centroids],
                c=range(self.cluster_number),
                cmap="cool",
                marker="x",
            )
            for i in range(self.cluster_number):
                plt.text(
                    self.centroids[i, 0],
                    self.centroids[i, 1],
                    i,
                    ha="center",
                    va="center",
                    fontsize=10,
                )
            plt.tight_layout()
            buf = io.BytesIO()
            plt.savefig(buf, format="png")
            buf.seek(0)
            self.pixmap = QPixmap()
            self.pixmap.loadFromData(buf.read())
            self.label.setPixmap(self.pixmap)
            plt.close()
        except Exception as e:
            self.statusbar.showMessage("Error Occured!")
            QMessageBox.warning(None, "Error", str(e))
        else:
            self.statusbar.showMessage("Done.")

    def on_actionGithubProject_triggered(self):
        QDesktopServices.openUrl("https://github.com/kongolou/dat-analysis-tool")

    # my code end
