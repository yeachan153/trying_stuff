def buildApp() {
    echo "building app"
}

def testApp() {
    echo "testing app"
}

def deployApp() {
    echo "deploy app ${params.VERSION}"
}

return this