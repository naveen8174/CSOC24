# Chall 1
here the code is in assembly form so our first task is to check with strings and all then we went with a reverse engineering tool named as [dog bolt](https://dogbolt.org/) there we can find the c similar code I found it in `Ghidra`  
the main function of the code went like this:
```
#include "out.h"



int _init(EVP_PKEY_CTX *ctx)

{
  int iVar1;
  
  iVar1 = _gmon_start_();
  return iVar1;
}



void FUN_00101020(void)

{
  (*(code *)(undefined *)0x0)();
  return;
}



void FUN_00101090(void)

{
  __cxa_finalize();
  return;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int puts(char *__s)

{
  int iVar1;
  
  iVar1 = puts(__s);
  return iVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

size_t strlen(char *__s)

{
  size_t sVar1;
  
  sVar1 = strlen(__s);
  return sVar1;
}



void __stack_chk_fail(void)

{
                    // WARNING: Subroutine does not return
  __stack_chk_fail();
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int printf(char *__format,...)

{
  int iVar1;
  
  iVar1 = printf(__format);
  return iVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

size_t strcspn(char *__s,char *__reject)

{
  size_t sVar1;
  
  sVar1 = strcspn(_s,_reject);
  return sVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

char * fgets(char *__s,int __n,FILE *__stream)

{
  char *pcVar1;
  
  pcVar1 = fgets(_s,n,_stream);
  return pcVar1;
}



void processEntry _start(undefined8 param_1,undefined8 param_2)

{
  undefined auStack_8 [8];
  
  __libc_start_main(main,param_2,&stack0x00000008,0,0,param_1,auStack_8);
  do {
                    // WARNING: Do nothing block with infinite loop
  } while( true );
}



// WARNING: Removing unreachable block (ram,0x00101143)
// WARNING: Removing unreachable block (ram,0x0010114f)

void deregister_tm_clones(void)

{
  return;
}



// WARNING: Removing unreachable block (ram,0x00101184)
// WARNING: Removing unreachable block (ram,0x00101190)

void register_tm_clones(void)

{
  return;
}



void __do_global_dtors_aux(void)

{
  if (completed_0 != '\0') {
    return;
  }
  FUN_00101090(__dso_handle);
  deregister_tm_clones();
  completed_0 = 1;
  return;
}



void frame_dummy(void)

{
  register_tm_clones();
  return;
}



undefined8 main(void)

{
  int iVar1;
  size_t sVar2;
  long in_FS_OFFSET;
  char local_118 [264];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  printf("What is the password:");
  fgets(local_118,0x100,stdin);
  sVar2 = strcspn(local_118,"\n");
  local_118[sVar2] = '\0';
  iVar1 = check(local_118);
  if (iVar1 == 1) {
    puts("Correct");
  }
  else {
    puts("Incorrect");
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    // WARNING: Subroutine does not return
    __stack_chk_fail();
  }
  return 0;
}



undefined8 check(char *param_1)

{
  size_t sVar1;
  undefined8 uVar2;
  
  sVar1 = strlen(param_1);
  if ((((int)sVar1 == 10) && (*param_1 == '1')) && (param_1[4] == '9')) {
    uVar2 = 1;
  }
  else {
    uVar2 = 0;
  }
  return uVar2;
}



void _fini(void)

{
  return;
}
```

for us most of the part is useless except the check function and the main function.
```
undefined8 check(char *param_1)

{
  size_t sVar1;
  undefined8 uVar2;
  
  sVar1 = strlen(param_1);
  if ((((int)sVar1 == 10) && (*param_1 == '1')) && (param_1[4] == '9')) {
    uVar2 = 1;
  }
  else {
    uVar2 = 0;
  }
```
here the password should have a length of 10 and first letter should be `1` and 5th letter should be `9` so by giving the appropriate password we get the value to be correct.

# Chall 2

Here again we use the above tool and generate the code we get the c++ code to be:  
```
uint64_t checkPassword(class std::string* arg1, int64_t arg2 @ r12)
{
    int64_t var_10 = arg2;
    void var_25;
    std::allocator<char>::allocator(&var_25);
    void var_48;
    std::string::string(&var_48, &data_2005);
    std::allocator<char>::~allocator(&var_25);
    int32_t var_20 = 0xfffffff9;
    int32_t rax = std::string::length(&var_48);
    int64_t rax_5;
    rax_5 = std::string::length(arg1) == -(var_20);
    int32_t rbx_2;
    if (rax_5 != 0)
    {
        void var_68;
        std::string::string(&var_68);
        for (int32_t i = 0; i < rax; i = (i + 1))
        {
            if (i == (rax - 1))
            {
                std::string::operator+=(&var_68);
                std::string::operator+=(&var_68);
            }
            std::string::operator+=(&var_68, *std::string::at(&var_48, i));
        }
        std::string::iterator rax_13 = std::string::end(arg1);
        std::reverse<__normal_iterator<char*, std::string> >(std::string::begin(arg1), rax_13);
        if (_ZSteqIcEN9__gnu_cxx11__enable_ifIXsrSt9__is_charIT_E7__valueEbE6__typeERKNSt7__cxx1112basic_stringIS3_St11char_traitsIS3_ESaIS3_EEESE_(arg1, &var_68) == 0)
        {
            rbx_2 = 1;
        }
        else
        {
            arg2 = 1;
            rbx_2 = 0;
        }
        std::string::~string(&var_68);
    }
    if ((rax_5 == 0 || (rax_5 != 0 && rbx_2 == 1)))
    {
        arg2 = 0;
    }
    std::string::~string(&var_48);
    return arg2;
}
```
here I used a handy tool named as `binary ninja` cloud version which gives us the control flow graphs and decompiled code here basically the code uses few variables from it's read only sight they are
```
data_2005
:64 65 63 00 dec.
data_2009
:6b 00 k.
data_200b
: 63 61 72 00 car.
``` 

here the variable var48_ continuously loaded `d`,`c` in to it and then loaded `k`, `car` and the loaded `c` to it and resulting in `dekcarc` and this word is compared with the reversed input string.  
so the password should be 
>cracked

# chall_3
