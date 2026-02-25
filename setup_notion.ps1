$claudeDir = Join-Path $env:USERPROFILE ".claude"
if (!(Test-Path $claudeDir)) {
  New-Item -ItemType Directory -Path $claudeDir -Force | Out-Null
}

$token = $env:NOTION_API_KEY  # Set via environment variable
$headerJson = '{"Authorization":"Bearer ' + $token + '","Notion-Version":"2022-06-28"}'

$settingsJson = @"
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "OPENAPI_MCP_HEADERS": "$headerJson"
      }
    }
  }
}
"@

$settingsPath = Join-Path $claudeDir "settings.json"
[System.IO.File]::WriteAllText($settingsPath, $settingsJson, [System.Text.Encoding]::UTF8)

Write-Host "=== Notion MCP Setup Complete ===" -ForegroundColor Green
Write-Host "Settings saved to: $settingsPath" -ForegroundColor Cyan
Write-Host ""
Write-Host "Content:" -ForegroundColor Yellow
Get-Content $settingsPath
