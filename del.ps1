
# ==========================================
# PowerShell Script: Reset All Django Migrations
# ==========================================

# List of your custom apps
$apps = @("carts","likes","playground","store","tags","users")

# Base path of your Django project (adjust if needed)
$basePath = "C:\dev\storefront"

foreach ($app in $apps) {
    $migrationsPath = Join-Path -Path $basePath -ChildPath "$app\migrations"
    
    if (Test-Path $migrationsPath) {
        Write-Host "Processing $app migrations..."
        
        # Optional: backup migrations first
        # $backupPath = Join-Path -Path $basePath -ChildPath "$app\migrations_backup"
        # Copy-Item -Path $migrationsPath -Destination $backupPath -Recurse -Force
        
        # Delete all 00*.py files except __init__.py
        Get-ChildItem -Path $migrationsPath -Filter "00*.py" | ForEach-Object {
            Remove-Item $_.FullName -Force
            Write-Host "Deleted: $($_.FullName)"
        }
    } else {
        Write-Host "Migrations folder not found for $app, skipping..."
    }
}

Write-Host "✅ All custom app migrations deleted. Keep __init__.py intact!"