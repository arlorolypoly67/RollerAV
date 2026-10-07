param(
    [Parameter(Mandatory)]
    [string]$CommitMessage
)

git.exe add .

if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

git.exe commit -m $CommitMessage

if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

git.exe push

if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}