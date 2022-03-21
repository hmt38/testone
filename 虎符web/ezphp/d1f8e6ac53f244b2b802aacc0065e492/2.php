<?php
highlight_file(__FILE__);
foreach($_REQUEST['envs'] as $key => $val) {
    putenv("{$key}={$val}");
}

system('echo hello');
?>