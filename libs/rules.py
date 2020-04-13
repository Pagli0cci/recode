rule = {}

rule['include'] = {
    'regText':"""(include|require)(_once){0,1}(\s{1,5}|\s{0,5}\().{0,60}\$(?!.*(this->))\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}""",
    'content':"文件包含函数中存在变量,可能存在文件包含漏洞"
}

rule['preg_replace'] = {
    'regText':"""preg_replace\(\s{0,5}.*/[is]{0,2}e[is]{0,2}["']\s{0,5},(.*\$.*,|.*,.*\$)""",
    'content':"preg_replace的/e模式，且有可控变量，可能存在代码执行漏洞"
}

rule['phpinfo'] = {
    'regText':"""phpinfo\s{0,5}\(\s{0,5}\)""",
    'content':"phpinfo()函数，可能存在敏感信息泄露漏洞"
}

rule['call_user_func'] = {
    'regText':"""call_user_func(_array){0,1}\(\s{0,5}\$\w{1,15}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}""",
    'content':"call_user_func函数参数包含变量，可能存在代码执行漏洞"
}

rule['readfile'] = {
    'regText':"""(file_get_contents|fopen|readfile|fgets|fread|parse_ini_file|highlight_file|fgetss|show_source)\s{0,5}\(.{0,40}\$\w{1,15}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}""",
    'content':"读取文件函数中存在变量，可能存在任意文件读取漏洞"
}


rule['systemexec'] = {
    'regText':"""(system|passthru|pcntl_exec|shell_exec|escapeshellcmd|exec|popen)\s{0,10}\(.{0,40}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}""",
    'content':"命令执行函数中存在变量，可能存在任意命令执行漏洞"
}

rule['parse_str'] = {
    'regText':"""(mb_){0,1}parse_str\s{0,10}\(.{0,40}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}""",
    'content':"parse_str函数中存在变量,可能存在变量覆盖漏洞"
}


rule['doublemoney'] = {
    'regText':"""\${{0,1}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}\s{0,4}=\s{0,4}.{0,20}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}""",
    'content':"双$$符号可能存在变量覆盖漏洞"
}


rule['ipinfo'] = {
    'regText':"""["'](HTTP_CLIENT_IP|HTTP_X_FORWARDED_FOR|HTTP_REFERER)["']""",
    'content':"获取IP地址方式可伪造，HTTP_REFERER可伪造，常见引发SQL注入等漏洞"
}


rule['filectrol'] = {
    'regText':"""(unlink|copy|fwrite|readfile|file_put_contents|file_get_contents|bzopen)\s{0,10}\(.{0,40}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}""",
    'content':"文件操作函数中存在变量，可能存在任意文件读取/删除/修改/写入等漏洞"
}

rule['extract'] = {
    'regText':"""(extract)\s{0,5}\(.{0,30}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}\s{0,5},{0,1}\s{0,5}(EXTR_OVERWRITE){0,1}\s{0,5}\)""",
    'content':"extract函数中存在变量，可能存在变量覆盖漏洞"
}


rule['codeexec'] = {
    'regText':"""\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}\s{0,5}\(\s{0,5}\$_(POST|GET|REQUEST|SERVER)\[.{1,20}\]""",
    'content':"可能存在代码执行漏洞,或者此处是后门"
}

rule['urldecode'] = {
    'regText':"""^(?!.*addslashes).{0,40}((raw){0,1}urldecode|stripslashes)\s{0,5}\(.{0,60}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}""",
    'content':"urldecode绕过GPC,stripslashes会取消GPC转义字符"
}


rule['double``'] = {
    'regText':"""`\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}`""",
    'content':"``反引号中包含变量，变量可控会导致命令执行漏洞"
}


rule['array_map'] = {
    'regText':"""array_map\s{0,4}\(\s{0,4}.{0,20}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}\s{0,4}.{0,20},""",
    'content':"array_map参数包含变量，变量可控可能会导致代码执行漏洞"
}

rule['sql_select'] = {
    'regText':"""select\s{1,4}.{1,60}from.{1,50}where\s{1,3}.{1,50}=["\s\.]{0,10}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}""",
    'content':"SQL语句select中条件变量无单引号保护，可能存在SQL注入漏洞"
}


rule['sql_delete'] = {
    'regText':"""delete\s{1,4}from.{1,20}where\s{1,3}.{1,30}=["\s\.]{0,10}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}""",
    'content':"SQL语句delete中条件变量无单引号保护，可能存在SQL注入漏洞"
}

rule['sql_insert'] = {
    'regText':"""insert\s{1,5}into\s{1,5}.{1,60}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}""",
    'content':"SQL语句insert中插入变量无单引号保护，可能存在SQL注入漏洞"
}

rule['sql_update'] = {
    'regText':"""update\s{1,4}.{1,30}\s{1,3}set\s{1,5}.{1,60}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}""",
    'content':"SQL语句delete中条件变量无单引号保护，可能存在SQL注入漏洞"
}

rule['eval'] = {
    'regText':"""(eval|assert)\s{0,10}\(.{0,60}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}""",
    'content':"eval或者assertc函数中存在变量，可能存在代码执行漏洞"
}

rule['echo'] = {
    'regText':"""(echo|print|print_r)\s{0,5}\({0,1}.{0,60}\$_(POST|GET|REQUEST|SERVER)""",
    'content':"echo等输出中存在可控变量，可能存在XSS漏洞"
}


rule['header'] = {
    'regText':"""(header\s{0,5}\(.{0,30}|window.location.href\s{0,5}=\s{0,5})\$_(POST|GET|REQUEST|SERVER)""",
    'content':"header函数或者js location有可控参数，存在任意跳转或http头污染漏洞"
}

rule['upload'] = {
    'regText':"""move_uploaded_file\s{0,5}\(""",
    'content':"存在文件上传，注意上传类型是否可控"
}


rule['unserialize'] = {
    'regText':"""(unserialize)\s{0,5}\({0,1}.{0,60}\$_(POST|GET|REQUEST|SERVER)""",
    'content':"unserialize函数中存在可控变量,可能存在反序列化漏洞"
}

rule['unserialize2'] = {
    'regText':"""(unserialize)\s{0,10}\(.{0,60}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}""",
    'content':"unserialize函数中存在变量,可能存在反序列化漏洞"
}