# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'platform-comms-app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tabTelemetry = QtWidgets.QWidget()
        self.tabTelemetry.setObjectName("tabTelemetry")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabTelemetry)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBoxTlm = QtWidgets.QGroupBox(self.tabTelemetry)
        self.groupBoxTlm.setMinimumSize(QtCore.QSize(0, 251))
        self.groupBoxTlm.setMaximumSize(QtCore.QSize(999999, 16777215))
        self.groupBoxTlm.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBoxTlm.setObjectName("groupBoxTlm")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBoxTlm)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayoutTlmCh = QtWidgets.QFormLayout()
        self.formLayoutTlmCh.setObjectName("formLayoutTlmCh")
        self.labelTlmChOne = QtWidgets.QLabel(self.groupBoxTlm)
        self.labelTlmChOne.setObjectName("labelTlmChOne")
        self.formLayoutTlmCh.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelTlmChOne)
        self.labelTlmChOneValue = QtWidgets.QLabel(self.groupBoxTlm)
        self.labelTlmChOneValue.setObjectName("labelTlmChOneValue")
        self.formLayoutTlmCh.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelTlmChOneValue)
        self.labelTlmChTwo = QtWidgets.QLabel(self.groupBoxTlm)
        self.labelTlmChTwo.setObjectName("labelTlmChTwo")
        self.formLayoutTlmCh.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelTlmChTwo)
        self.labelTlmChThree = QtWidgets.QLabel(self.groupBoxTlm)
        self.labelTlmChThree.setObjectName("labelTlmChThree")
        self.formLayoutTlmCh.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelTlmChThree)
        self.labelTlmChTwoValue = QtWidgets.QLabel(self.groupBoxTlm)
        self.labelTlmChTwoValue.setObjectName("labelTlmChTwoValue")
        self.formLayoutTlmCh.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelTlmChTwoValue)
        self.labelTlmChThreeValue = QtWidgets.QLabel(self.groupBoxTlm)
        self.labelTlmChThreeValue.setObjectName("labelTlmChThreeValue")
        self.formLayoutTlmCh.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelTlmChThreeValue)
        self.verticalLayout_5.addLayout(self.formLayoutTlmCh)
        self.boxLayoutAdHocReq = QtWidgets.QVBoxLayout()
        self.boxLayoutAdHocReq.setObjectName("boxLayoutAdHocReq")
        self.groupBoxAdHocReq = QtWidgets.QGroupBox(self.groupBoxTlm)
        self.groupBoxAdHocReq.setObjectName("groupBoxAdHocReq")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBoxAdHocReq)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBoxTlmErr = QtWidgets.QGroupBox(self.groupBoxAdHocReq)
        self.groupBoxTlmErr.setObjectName("groupBoxTlmErr")
        self.labelTlmErrChannel = QtWidgets.QLabel(self.groupBoxTlmErr)
        self.labelTlmErrChannel.setGeometry(QtCore.QRect(20, 40, 60, 16))
        self.labelTlmErrChannel.setObjectName("labelTlmErrChannel")
        self.labelTlmErrChannelValue = QtWidgets.QLabel(self.groupBoxTlmErr)
        self.labelTlmErrChannelValue.setGeometry(QtCore.QRect(90, 40, 60, 16))
        self.labelTlmErrChannelValue.setObjectName("labelTlmErrChannelValue")
        self.labelTlmErrReason = QtWidgets.QLabel(self.groupBoxTlmErr)
        self.labelTlmErrReason.setGeometry(QtCore.QRect(180, 40, 60, 16))
        self.labelTlmErrReason.setObjectName("labelTlmErrReason")
        self.labelTlmErrReasonValue = QtWidgets.QLabel(self.groupBoxTlmErr)
        self.labelTlmErrReasonValue.setGeometry(QtCore.QRect(230, 40, 60, 16))
        self.labelTlmErrReasonValue.setObjectName("labelTlmErrReasonValue")
        self.gridLayout_6.addWidget(self.groupBoxTlmErr, 5, 1, 2, 5)
        self.pushButtonSendTlmReq = QtWidgets.QPushButton(self.groupBoxAdHocReq)
        self.pushButtonSendTlmReq.setObjectName("pushButtonSendTlmReq")
        self.gridLayout_6.addWidget(self.pushButtonSendTlmReq, 0, 0, 1, 1)
        self.labelTlmAdHocChannel = QtWidgets.QLabel(self.groupBoxAdHocReq)
        self.labelTlmAdHocChannel.setObjectName("labelTlmAdHocChannel")
        self.gridLayout_6.addWidget(self.labelTlmAdHocChannel, 0, 1, 1, 1)
        self.formLayoutTlmTimeouts = QtWidgets.QFormLayout()
        self.formLayoutTlmTimeouts.setObjectName("formLayoutTlmTimeouts")
        self.labelTlmTimeouts = QtWidgets.QLabel(self.groupBoxAdHocReq)
        self.labelTlmTimeouts.setObjectName("labelTlmTimeouts")
        self.formLayoutTlmTimeouts.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelTlmTimeouts)
        self.labelTlmTimeoutValue = QtWidgets.QLabel(self.groupBoxAdHocReq)
        self.labelTlmTimeoutValue.setObjectName("labelTlmTimeoutValue")
        self.formLayoutTlmTimeouts.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelTlmTimeoutValue)
        self.gridLayout_6.addLayout(self.formLayoutTlmTimeouts, 0, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 0, 4, 1, 1)
        self.checkBoxTlmReqContinuous = QtWidgets.QCheckBox(self.groupBoxAdHocReq)
        self.checkBoxTlmReqContinuous.setObjectName("checkBoxTlmReqContinuous")
        self.gridLayout_6.addWidget(self.checkBoxTlmReqContinuous, 5, 0, 1, 1)
        self.spinBoxTlmAdHocChValue = QtWidgets.QSpinBox(self.groupBoxAdHocReq)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxTlmAdHocChValue.sizePolicy().hasHeightForWidth())
        self.spinBoxTlmAdHocChValue.setSizePolicy(sizePolicy)
        self.spinBoxTlmAdHocChValue.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBoxTlmAdHocChValue.setProperty("showGroupSeparator", False)
        self.spinBoxTlmAdHocChValue.setProperty("value", 0)
        self.spinBoxTlmAdHocChValue.setObjectName("spinBoxTlmAdHocChValue")
        self.gridLayout_6.addWidget(self.spinBoxTlmAdHocChValue, 0, 3, 1, 1)
        self.boxLayoutAdHocReq.addWidget(self.groupBoxAdHocReq)
        self.verticalLayout_5.addLayout(self.boxLayoutAdHocReq)
        self.verticalLayout_4.addWidget(self.groupBoxTlm)
        self.tabWidget.addTab(self.tabTelemetry, "")
        self.tabTelecommanding = QtWidgets.QWidget()
        self.tabTelecommanding.setObjectName("tabTelecommanding")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabTelecommanding)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxTelecommanding = QtWidgets.QGroupBox(self.tabTelecommanding)
        self.groupBoxTelecommanding.setMinimumSize(QtCore.QSize(0, 251))
        self.groupBoxTelecommanding.setMaximumSize(QtCore.QSize(999999, 16777215))
        self.groupBoxTelecommanding.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBoxTelecommanding.setObjectName("groupBoxTelecommanding")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxTelecommanding)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayoutTc = QtWidgets.QFormLayout()
        self.formLayoutTc.setObjectName("formLayoutTc")
        self.labelTcNumber = QtWidgets.QLabel(self.groupBoxTelecommanding)
        self.labelTcNumber.setObjectName("labelTcNumber")
        self.formLayoutTc.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelTcNumber)
        self.spinBoxTcNumberValue = QtWidgets.QSpinBox(self.groupBoxTelecommanding)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxTcNumberValue.sizePolicy().hasHeightForWidth())
        self.spinBoxTcNumberValue.setSizePolicy(sizePolicy)
        self.spinBoxTcNumberValue.setInputMethodHints(QtCore.Qt.ImhNone)
        self.spinBoxTcNumberValue.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBoxTcNumberValue.setObjectName("spinBoxTcNumberValue")
        self.formLayoutTc.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBoxTcNumberValue)
        self.gridLayout_3.addLayout(self.formLayoutTc, 0, 0, 1, 1)
        self.pushButtonSendTcReq = QtWidgets.QPushButton(self.groupBoxTelecommanding)
        self.pushButtonSendTcReq.setObjectName("pushButtonSendTcReq")
        self.gridLayout_3.addWidget(self.pushButtonSendTcReq, 5, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.verticalLayoutTimeCommands = QtWidgets.QVBoxLayout()
        self.verticalLayoutTimeCommands.setObjectName("verticalLayoutTimeCommands")
        self.groupBoxTimeCommands = QtWidgets.QGroupBox(self.groupBoxTelecommanding)
        self.groupBoxTimeCommands.setObjectName("groupBoxTimeCommands")
        self.pushButtonSendPcTime = QtWidgets.QPushButton(self.groupBoxTimeCommands)
        self.pushButtonSendPcTime.setGeometry(QtCore.QRect(9, 29, 128, 32))
        self.pushButtonSendPcTime.setObjectName("pushButtonSendPcTime")
        self.layoutWidget = QtWidgets.QWidget(self.groupBoxTimeCommands)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 60, 377, 38))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayoutSendTime = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayoutSendTime.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutSendTime.setObjectName("horizontalLayoutSendTime")
        self.pushButtonSendThisTime = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonSendThisTime.setObjectName("pushButtonSendThisTime")
        self.horizontalLayoutSendTime.addWidget(self.pushButtonSendThisTime)
        self.horizontalLayoutSendTimeValues = QtWidgets.QHBoxLayout()
        self.horizontalLayoutSendTimeValues.setObjectName("horizontalLayoutSendTimeValues")
        self.dateEditSendThisDate = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEditSendThisDate.setObjectName("dateEditSendThisDate")
        self.horizontalLayoutSendTimeValues.addWidget(self.dateEditSendThisDate, 0, QtCore.Qt.AlignLeft)
        self.dateTimeEditSendThisTime = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEditSendThisTime.setObjectName("dateTimeEditSendThisTime")
        self.horizontalLayoutSendTimeValues.addWidget(self.dateTimeEditSendThisTime)
        self.horizontalLayoutSendTime.addLayout(self.horizontalLayoutSendTimeValues)
        self.verticalLayoutTimeCommands.addWidget(self.groupBoxTimeCommands)
        self.groupBoxLastResponse = QtWidgets.QGroupBox(self.groupBoxTelecommanding)
        self.groupBoxLastResponse.setObjectName("groupBoxLastResponse")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBoxLastResponse)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.formLayoutTcN = QtWidgets.QFormLayout()
        self.formLayoutTcN.setObjectName("formLayoutTcN")
        self.labelTcResNumber = QtWidgets.QLabel(self.groupBoxLastResponse)
        self.labelTcResNumber.setObjectName("labelTcResNumber")
        self.formLayoutTcN.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelTcResNumber)
        self.labelTcResNumberValue = QtWidgets.QLabel(self.groupBoxLastResponse)
        self.labelTcResNumberValue.setObjectName("labelTcResNumberValue")
        self.formLayoutTcN.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelTcResNumberValue)
        self.gridLayout_5.addLayout(self.formLayoutTcN, 0, 0, 1, 1)
        self.formLayoutTimeouts = QtWidgets.QFormLayout()
        self.formLayoutTimeouts.setObjectName("formLayoutTimeouts")
        self.labelTcResTimeouts = QtWidgets.QLabel(self.groupBoxLastResponse)
        self.labelTcResTimeouts.setObjectName("labelTcResTimeouts")
        self.formLayoutTimeouts.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelTcResTimeouts)
        self.labelTcResTimeoutsValue = QtWidgets.QLabel(self.groupBoxLastResponse)
        self.labelTcResTimeoutsValue.setObjectName("labelTcResTimeoutsValue")
        self.formLayoutTimeouts.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelTcResTimeoutsValue)
        self.gridLayout_5.addLayout(self.formLayoutTimeouts, 0, 1, 1, 1)
        self.formLayoutTcResponse = QtWidgets.QFormLayout()
        self.formLayoutTcResponse.setObjectName("formLayoutTcResponse")
        self.labelTcRes = QtWidgets.QLabel(self.groupBoxLastResponse)
        self.labelTcRes.setObjectName("labelTcRes")
        self.formLayoutTcResponse.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelTcRes)
        self.labelTcResStatus = QtWidgets.QLabel(self.groupBoxLastResponse)
        self.labelTcResStatus.setObjectName("labelTcResStatus")
        self.formLayoutTcResponse.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelTcResStatus)
        self.gridLayout_5.addLayout(self.formLayoutTcResponse, 1, 0, 1, 1)
        self.verticalLayoutTimeCommands.addWidget(self.groupBoxLastResponse)
        self.gridLayout_3.addLayout(self.verticalLayoutTimeCommands, 6, 0, 1, 3)
        self.checkBoxTcReqContinuous = QtWidgets.QCheckBox(self.groupBoxTelecommanding)
        self.checkBoxTcReqContinuous.setObjectName("checkBoxTcReqContinuous")
        self.gridLayout_3.addWidget(self.checkBoxTcReqContinuous, 1, 1, 1, 1)
        self.comboBoxTcDataType = QtWidgets.QComboBox(self.groupBoxTelecommanding)
        self.comboBoxTcDataType.setObjectName("comboBoxTcDataType")
        self.comboBoxTcDataType.addItem("")
        self.comboBoxTcDataType.addItem("")
        self.comboBoxTcDataType.addItem("")
        self.gridLayout_3.addWidget(self.comboBoxTcDataType, 0, 2, 1, 1)
        self.formLayoutTcData = QtWidgets.QFormLayout()
        self.formLayoutTcData.setObjectName("formLayoutTcData")
        self.labelTcData = QtWidgets.QLabel(self.groupBoxTelecommanding)
        self.labelTcData.setObjectName("labelTcData")
        self.formLayoutTcData.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelTcData)
        self.inputTcData = QtWidgets.QLineEdit(self.groupBoxTelecommanding)
        self.inputTcData.setInputMethodHints(QtCore.Qt.ImhNone)
        self.inputTcData.setObjectName("inputTcData")
        self.formLayoutTcData.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputTcData)
        self.gridLayout_3.addLayout(self.formLayoutTcData, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxTelecommanding)
        self.tabWidget.addTab(self.tabTelecommanding, "")
        self.tabFileTransfer = QtWidgets.QWidget()
        self.tabFileTransfer.setObjectName("tabFileTransfer")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabFileTransfer)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBoxToUpload = QtWidgets.QGroupBox(self.tabFileTransfer)
        self.groupBoxToUpload.setObjectName("groupBoxToUpload")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBoxToUpload)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayoutToUpload = QtWidgets.QVBoxLayout()
        self.verticalLayoutToUpload.setObjectName("verticalLayoutToUpload")
        self.formLayoutUploadToFrom = QtWidgets.QFormLayout()
        self.formLayoutUploadToFrom.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayoutUploadToFrom.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayoutUploadToFrom.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayoutUploadToFrom.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayoutUploadToFrom.setObjectName("formLayoutUploadToFrom")
        self.labelUploadTo = QtWidgets.QLabel(self.groupBoxToUpload)
        self.labelUploadTo.setObjectName("labelUploadTo")
        self.formLayoutUploadToFrom.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelUploadTo)
        self.lineEditUploadTo = QtWidgets.QLineEdit(self.groupBoxToUpload)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditUploadTo.sizePolicy().hasHeightForWidth())
        self.lineEditUploadTo.setSizePolicy(sizePolicy)
        self.lineEditUploadTo.setObjectName("lineEditUploadTo")
        self.formLayoutUploadToFrom.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditUploadTo)
        self.labelUploadFrom = QtWidgets.QLabel(self.groupBoxToUpload)
        self.labelUploadFrom.setObjectName("labelUploadFrom")
        self.formLayoutUploadToFrom.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelUploadFrom)
        self.horizontalLayoutUploadFrom = QtWidgets.QHBoxLayout()
        self.horizontalLayoutUploadFrom.setObjectName("horizontalLayoutUploadFrom")
        self.lineEditUploadFrom = QtWidgets.QLineEdit(self.groupBoxToUpload)
        self.lineEditUploadFrom.setObjectName("lineEditUploadFrom")
        self.horizontalLayoutUploadFrom.addWidget(self.lineEditUploadFrom)
        self.pushButtonOpenFileUploadFrom = QtWidgets.QPushButton(self.groupBoxToUpload)
        self.pushButtonOpenFileUploadFrom.setObjectName("pushButtonOpenFileUploadFrom")
        self.horizontalLayoutUploadFrom.addWidget(self.pushButtonOpenFileUploadFrom)
        self.formLayoutUploadToFrom.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayoutUploadFrom)
        self.verticalLayoutToUpload.addLayout(self.formLayoutUploadToFrom)
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        self.pushButtonUploadFile = QtWidgets.QPushButton(self.groupBoxToUpload)
        self.pushButtonUploadFile.setObjectName("pushButtonUploadFile")
        self.horizontalLayout1.addWidget(self.pushButtonUploadFile)
        self.pushButtonAbortUploadFile = QtWidgets.QPushButton(self.groupBoxToUpload)
        self.pushButtonAbortUploadFile.setObjectName("pushButtonAbortUploadFile")
        self.horizontalLayout1.addWidget(self.pushButtonAbortUploadFile)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout1.addItem(spacerItem1)
        self.verticalLayoutToUpload.addLayout(self.horizontalLayout1)
        self.progressBarUpload = QtWidgets.QProgressBar(self.groupBoxToUpload)
        self.progressBarUpload.setProperty("value", 24)
        self.progressBarUpload.setObjectName("progressBarUpload")
        self.verticalLayoutToUpload.addWidget(self.progressBarUpload)
        self.verticalLayout_7.addLayout(self.verticalLayoutToUpload)
        self.gridLayout_2.addWidget(self.groupBoxToUpload, 0, 0, 1, 1)
        self.groupBoxToDownload = QtWidgets.QGroupBox(self.tabFileTransfer)
        self.groupBoxToDownload.setObjectName("groupBoxToDownload")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBoxToDownload)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.formLayoutDownloadFromTo = QtWidgets.QFormLayout()
        self.formLayoutDownloadFromTo.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayoutDownloadFromTo.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayoutDownloadFromTo.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayoutDownloadFromTo.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayoutDownloadFromTo.setObjectName("formLayoutDownloadFromTo")
        self.labelDownloadFrom = QtWidgets.QLabel(self.groupBoxToDownload)
        self.labelDownloadFrom.setObjectName("labelDownloadFrom")
        self.formLayoutDownloadFromTo.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelDownloadFrom)
        self.lineEditDownloadFrom = QtWidgets.QLineEdit(self.groupBoxToDownload)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDownloadFrom.sizePolicy().hasHeightForWidth())
        self.lineEditDownloadFrom.setSizePolicy(sizePolicy)
        self.lineEditDownloadFrom.setObjectName("lineEditDownloadFrom")
        self.formLayoutDownloadFromTo.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditDownloadFrom)
        self.labelDownloadTo = QtWidgets.QLabel(self.groupBoxToDownload)
        self.labelDownloadTo.setObjectName("labelDownloadTo")
        self.formLayoutDownloadFromTo.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelDownloadTo)
        self.horizontalLayoutDownloadTo = QtWidgets.QHBoxLayout()
        self.horizontalLayoutDownloadTo.setObjectName("horizontalLayoutDownloadTo")
        self.lineEditDownloadTo = QtWidgets.QLineEdit(self.groupBoxToDownload)
        self.lineEditDownloadTo.setObjectName("lineEditDownloadTo")
        self.horizontalLayoutDownloadTo.addWidget(self.lineEditDownloadTo)
        self.pushButtonOpenFileDownloadTo = QtWidgets.QPushButton(self.groupBoxToDownload)
        self.pushButtonOpenFileDownloadTo.setObjectName("pushButtonOpenFileDownloadTo")
        self.horizontalLayoutDownloadTo.addWidget(self.pushButtonOpenFileDownloadTo)
        self.formLayoutDownloadFromTo.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayoutDownloadTo)
        self.verticalLayout_8.addLayout(self.formLayoutDownloadFromTo)
        self.horizontalLayoutRequestDownload = QtWidgets.QHBoxLayout()
        self.horizontalLayoutRequestDownload.setObjectName("horizontalLayoutRequestDownload")
        self.pushButtonRequestDownload = QtWidgets.QPushButton(self.groupBoxToDownload)
        self.pushButtonRequestDownload.setObjectName("pushButtonRequestDownload")
        self.horizontalLayoutRequestDownload.addWidget(self.pushButtonRequestDownload)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutRequestDownload.addItem(spacerItem2)
        self.verticalLayout_8.addLayout(self.horizontalLayoutRequestDownload)
        self.progressBarDownload = QtWidgets.QProgressBar(self.groupBoxToDownload)
        self.progressBarDownload.setProperty("value", 24)
        self.progressBarDownload.setObjectName("progressBarDownload")
        self.verticalLayout_8.addWidget(self.progressBarDownload)
        self.gridLayout_2.addWidget(self.groupBoxToDownload, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabFileTransfer, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tabConfig = QtWidgets.QWidget()
        self.tabConfig.setObjectName("tabConfig")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tabConfig)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBoxConfig = QtWidgets.QGroupBox(self.tabConfig)
        self.groupBoxConfig.setObjectName("groupBoxConfig")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBoxConfig)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.formLayoutConfig = QtWidgets.QFormLayout()
        self.formLayoutConfig.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayoutConfig.setObjectName("formLayoutConfig")
        self.labelCommsBaud = QtWidgets.QLabel(self.groupBoxConfig)
        self.labelCommsBaud.setObjectName("labelCommsBaud")
        self.formLayoutConfig.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelCommsBaud)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.comboBoxCommsBaudValue = QtWidgets.QComboBox(self.groupBoxConfig)
        self.comboBoxCommsBaudValue.setObjectName("comboBoxCommsBaudValue")
        self.comboBoxCommsBaudValue.addItem("")
        self.comboBoxCommsBaudValue.addItem("")
        self.comboBoxCommsBaudValue.addItem("")
        self.comboBoxCommsBaudValue.addItem("")
        self.comboBoxCommsBaudValue.addItem("")
        self.comboBoxCommsBaudValue.addItem("")
        self.comboBoxCommsBaudValue.addItem("")
        self.comboBoxCommsBaudValue.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBoxCommsBaudValue)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.labelTcTlmRate = QtWidgets.QLabel(self.groupBoxConfig)
        self.labelTcTlmRate.setObjectName("labelTcTlmRate")
        self.horizontalLayout_8.addWidget(self.labelTcTlmRate)
        self.spinBoxTcTlmRateValue = QtWidgets.QSpinBox(self.groupBoxConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxTcTlmRateValue.sizePolicy().hasHeightForWidth())
        self.spinBoxTcTlmRateValue.setSizePolicy(sizePolicy)
        self.spinBoxTcTlmRateValue.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBoxTcTlmRateValue.setProperty("value", 1)
        self.spinBoxTcTlmRateValue.setObjectName("spinBoxTcTlmRateValue")
        self.horizontalLayout_8.addWidget(self.spinBoxTcTlmRateValue)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.labelTcTlmTimeout = QtWidgets.QLabel(self.groupBoxConfig)
        self.labelTcTlmTimeout.setObjectName("labelTcTlmTimeout")
        self.horizontalLayout_8.addWidget(self.labelTcTlmTimeout)
        self.spinBoxTcTlmTimeoutValue = QtWidgets.QSpinBox(self.groupBoxConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxTcTlmTimeoutValue.sizePolicy().hasHeightForWidth())
        self.spinBoxTcTlmTimeoutValue.setSizePolicy(sizePolicy)
        self.spinBoxTcTlmTimeoutValue.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBoxTcTlmTimeoutValue.setObjectName("spinBoxTcTlmTimeoutValue")
        self.horizontalLayout_8.addWidget(self.spinBoxTcTlmTimeoutValue)
        self.formLayoutConfig.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_8)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayoutConfig.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem5)
        self.labelConfigFile = QtWidgets.QLabel(self.groupBoxConfig)
        self.labelConfigFile.setObjectName("labelConfigFile")
        self.formLayoutConfig.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelConfigFile)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEditConfigFilePath = QtWidgets.QLineEdit(self.groupBoxConfig)
        self.lineEditConfigFilePath.setObjectName("lineEditConfigFilePath")
        self.horizontalLayout_9.addWidget(self.lineEditConfigFilePath)
        self.pushButtonOpenConfigFilePath = QtWidgets.QPushButton(self.groupBoxConfig)
        self.pushButtonOpenConfigFilePath.setObjectName("pushButtonOpenConfigFilePath")
        self.horizontalLayout_9.addWidget(self.pushButtonOpenConfigFilePath)
        self.formLayoutConfig.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_9)
        self.gridLayout_10.addLayout(self.formLayoutConfig, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBoxConfig, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tabConfig, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(4)
        self.pushButtonSendPcTime.clicked.connect(Form.on_send_pc_time)
        self.pushButtonSendThisTime.clicked.connect(Form.on_click_this_time)
        self.pushButtonSendTcReq.clicked.connect(Form.on_click_send_telecommand_request)
        self.pushButtonSendTlmReq.clicked.connect(Form.on_click_send_telemetry_request)
        self.pushButtonUploadFile.clicked.connect(Form.on_click_upload_open)
        self.pushButtonRequestDownload.clicked.connect(Form.on_click_download_open)
        self.pushButtonAbortUploadFile.clicked.connect(Form.on_click_upload_abort)
        self.comboBoxCommsBaudValue.currentTextChanged['QString'].connect(Form.on_baud_rate_change)
        self.spinBoxTcTlmRateValue.valueChanged['int'].connect(Form.on_tc_tlm_rate_change)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "OSSAT Platform Computer Comms"))
        self.groupBoxTlm.setTitle(_translate("Form", "Telemetry"))
        self.labelTlmChOne.setText(_translate("Form", "TLM CH 1"))
        self.labelTlmChOneValue.setText(_translate("Form", "N/A"))
        self.labelTlmChTwo.setText(_translate("Form", "TLM CH 2"))
        self.labelTlmChThree.setText(_translate("Form", "TLM CH 3"))
        self.labelTlmChTwoValue.setText(_translate("Form", "N/A"))
        self.labelTlmChThreeValue.setText(_translate("Form", "N/A"))
        self.groupBoxAdHocReq.setTitle(_translate("Form", "Ad-hoc Request"))
        self.groupBoxTlmErr.setTitle(_translate("Form", "Last Failure"))
        self.labelTlmErrChannel.setText(_translate("Form", "Channel #"))
        self.labelTlmErrChannelValue.setText(_translate("Form", "N/A"))
        self.labelTlmErrReason.setText(_translate("Form", "Reason"))
        self.labelTlmErrReasonValue.setText(_translate("Form", "N/A"))
        self.pushButtonSendTlmReq.setText(_translate("Form", "Send TLM REQ"))
        self.labelTlmAdHocChannel.setText(_translate("Form", "Channel #"))
        self.labelTlmTimeouts.setText(_translate("Form", "TIMEOUTS:"))
        self.labelTlmTimeoutValue.setText(_translate("Form", "N/A"))
        self.checkBoxTlmReqContinuous.setText(_translate("Form", "Continuous?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTelemetry), _translate("Form", "TELEMETRY"))
        self.groupBoxTelecommanding.setTitle(_translate("Form", "Telecommanding"))
        self.labelTcNumber.setText(_translate("Form", "TC #"))
        self.pushButtonSendTcReq.setText(_translate("Form", "Send TC REQ"))
        self.groupBoxTimeCommands.setTitle(_translate("Form", "Time Commands"))
        self.pushButtonSendPcTime.setText(_translate("Form", "Send PC Time"))
        self.pushButtonSendThisTime.setText(_translate("Form", "Send this Time :"))
        self.dateTimeEditSendThisTime.setDisplayFormat(_translate("Form", "HH:mm:ss.zzz"))
        self.groupBoxLastResponse.setTitle(_translate("Form", "Last Response"))
        self.labelTcResNumber.setText(_translate("Form", "TC #"))
        self.labelTcResNumberValue.setText(_translate("Form", "N"))
        self.labelTcResTimeouts.setText(_translate("Form", "TIMEOUTS :"))
        self.labelTcResTimeoutsValue.setText(_translate("Form", "N/A"))
        self.labelTcRes.setText(_translate("Form", "Response"))
        self.labelTcResStatus.setText(_translate("Form", "N/A"))
        self.checkBoxTcReqContinuous.setText(_translate("Form", "Continuous?"))
        self.comboBoxTcDataType.setItemText(0, _translate("Form", "String"))
        self.comboBoxTcDataType.setItemText(1, _translate("Form", "Integer"))
        self.comboBoxTcDataType.setItemText(2, _translate("Form", "Floating Point"))
        self.labelTcData.setText(_translate("Form", "Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTelecommanding), _translate("Form", "TELECOMMANDING"))
        self.groupBoxToUpload.setTitle(_translate("Form", "To Upload"))
        self.labelUploadTo.setText(_translate("Form", "Upload to:"))
        self.labelUploadFrom.setText(_translate("Form", "Upload from:"))
        self.pushButtonOpenFileUploadFrom.setText(_translate("Form", "..."))
        self.pushButtonUploadFile.setText(_translate("Form", "Upload Now"))
        self.pushButtonAbortUploadFile.setText(_translate("Form", "Abort Upload"))
        self.groupBoxToDownload.setTitle(_translate("Form", "To Download"))
        self.labelDownloadFrom.setText(_translate("Form", "Download from:"))
        self.labelDownloadTo.setText(_translate("Form", "Download to:"))
        self.pushButtonOpenFileDownloadTo.setText(_translate("Form", "..."))
        self.pushButtonRequestDownload.setText(_translate("Form", "Request Download"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFileTransfer), _translate("Form", "FILE TRANSFER"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "LOG"))
        self.groupBoxConfig.setTitle(_translate("Form", "Config"))
        self.labelCommsBaud.setText(_translate("Form", "Comms baud"))
        self.comboBoxCommsBaudValue.setItemText(0, _translate("Form", "9600"))
        self.comboBoxCommsBaudValue.setItemText(1, _translate("Form", "19200"))
        self.comboBoxCommsBaudValue.setItemText(2, _translate("Form", "38400"))
        self.comboBoxCommsBaudValue.setItemText(3, _translate("Form", "57600"))
        self.comboBoxCommsBaudValue.setItemText(4, _translate("Form", "115200"))
        self.comboBoxCommsBaudValue.setItemText(5, _translate("Form", "230400"))
        self.comboBoxCommsBaudValue.setItemText(6, _translate("Form", "460800"))
        self.comboBoxCommsBaudValue.setItemText(7, _translate("Form", "921600"))
        self.labelTcTlmRate.setText(_translate("Form", "TC/TLM Rate (per second)"))
        self.labelTcTlmTimeout.setText(_translate("Form", "TC/TLM Timeout (ms)"))
        self.labelConfigFile.setText(_translate("Form", "Config file"))
        self.pushButtonOpenConfigFilePath.setText(_translate("Form", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConfig), _translate("Form", "CONFIG"))
