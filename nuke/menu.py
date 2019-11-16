toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("OCIO", icon="OCIO_logo.png")
m.addCommand("OCIO transforms", "nuke.createNode('OCIOtransforms')", icon = "OCIO_logo.png")