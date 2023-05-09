strace -p <PID of Apache>
curl -v http://localhost:80
file { '/path/to/affected/file':
  owner => 'apache',
  group => 'apache',
  mode  => '0644',
}

