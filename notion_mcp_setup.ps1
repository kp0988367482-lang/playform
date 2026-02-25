
# Notion MCP 설정 스크립트
$claudeDir = "$env:USERPROFILE\.claude"
$settingsPath = "$claudeDir\settings.json"

# .claude 디렉토리 생성
if (!(Test-Path $claudeDir)) {
    New-Item -ItemType Directory -Path $claudeDir -Force | Out-Null
    Write-Host ".claude 디렉토리 생성됨" -ForegroundColor Green
}

# 기존 설정 읽기 또는 새 설정 생성
if (Test-Path $settingsPath) {
    $settings = Get-Content $settingsPath | ConvertFrom-Json
    Write-Host "기존 settings.json 을 읽었습니다." -ForegroundColor Yellow
}
else {
    $settings = [PSCustomObject]@{}
    Write-Host "새 settings.json 을 생성합니다." -ForegroundColor Green
}

# MCP 서버 설정 추가
$notionServer = [PSCustomObject]@{
    command = "npx"
    args    = @("-y", "@notionhq/notion-mcp-server")
    env     = [PSCustomObject]@{
        OPENAPI_MCP_HEADERS = '{"Authorization":"Bearer ' + $env:NOTION_API_KEY + '","Notion-Version":"2022-06-28"}'
    }
}

if (-not $settings.PSObject.Properties['mcpServers']) {
    $settings | Add-Member -MemberType NoteProperty -Name 'mcpServers' -Value ([PSCustomObject]@{})
}

$settings.mcpServers | Add-Member -MemberType NoteProperty -Name 'notion' -Value $notionServer -Force

# 파일 저장
$settings | ConvertTo-Json -Depth 10 | Set-Content $settingsPath -Encoding UTF8

Write-Host ""
Write-Host "✅ Notion MCP 설정 완료!" -ForegroundColor Green
Write-Host "📄 설정 파일: $settingsPath" -ForegroundColor Cyan
Write-Host ""
Write-Host "다음 단계:" -ForegroundColor Yellow
Write-Host "1. VS Code를 재시작하세요"
Write-Host "2. Claude Code 패널에서 /mcp 명령으로 notion 서버 확인"
Write-Host "3. Notion 페이지에 Integration 연결 필요:"
Write-Host "   - Notion 페이지 열기 → ••• 메뉴 → Connections → 'Claude MCP' 추가"
