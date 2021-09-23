# files on this

**0-current_working_directory**
```
#!/bin/bash
pwd
```
**10-back**
```
#!/bin/bash
cd -
```
**11-lists**
```
#!/bin/bash
ls -la . .. /boot
```
**12-file_type**
```
#!/bin/bash
file /tmp/iamafile
```
**13-symbolic_link**
```
#!/bin/bash
ln -s /bin/ls __ls__
```
**14-copy_html**
```
#!/bin/bash
cp -rn *.html ..
```
**15-lets_move**
```
#!/bin/bash
mv [[:upper:]]* /tmp/u/
```
**16-clean_emacs**
```
#!/bin/bash
rm *~
```
**17-tree**
```
#!/bin/bash
mkdir -p welcome/to/school
```
**18-commas**
```
#!/bin/bash
ls -apxm
```
**1-listit**
```
#!/bin/bash
ls
```
**2-bring_me_home**
```
#!/bin/bash
cd
```
**3-listfiles**
```
#!/bin/bash
ls -l
```
**4-listmorefiles**
```
#!/bin/bash
ls -la .
```
**5-listfilesdigitonly**
```
#!/bin/bash
ls -al .
```
**6-firstdirectory**
```
#!/bin/bash
mkdir /tmp/my_first_directory
```
**7-movethatfile**
```
#!/bin/bash
mv /tmp/betty /tmp/my_first_directory
```
**8-firstdelete**
```
#!/bin/bash
rm /tmp/my_first_directory/betty
```
**9-firstdirdeletion**
```
#!/bin/bash
rmdir /tmp/my_first_directory
```
**school.mgc**
```
0 string SCHOOL School data
!:mime School
```