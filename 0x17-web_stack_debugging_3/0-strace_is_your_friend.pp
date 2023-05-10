# A puppet script to trance and fix a typo error line in a file on a server
$file_root = '/var/www/html/wp-settings.php'
#replace line containing "phpp" with "php"
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_root}",
  path    => ['/bin','/usr/bin']
}
