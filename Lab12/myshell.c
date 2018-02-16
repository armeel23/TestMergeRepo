void main()
{
	char* shell = getenv("MYSHELL");
	if (shell)
	{
		shell = 0xb7f9aad4;
		printf("%08x\n", shell);
		printf("%c\n", *shell);
		printf("%c\n", *(shell+1));
		printf("%c\n", *(shell+2));
		printf("%c\n", *(shell+3));
		printf("%c\n", *(shell+4));
		printf("%c\n", *(shell+5));
		printf("%c\n", *(shell+6));
		printf("%c\n", *(shell+7));
	}
}
