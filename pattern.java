// class NewPattern 
// {
// 	public static void main(String[] args) 
// 	{
// 		int i,j;
// 		for(i=1;i<=5;i++){
// 			for(j=1;j<=5;j++){
// 				if(j>=i){
// 					System.out.print(" ");
// 				}
// 				else{
// 					System.out.print(" * ");
// 				}
// 			}
// 			System.out.println();
// 		}
// 	}
// }
class Pattern16 
{
	public static void main(String[] args) 
	{
		int i,j,k;
		for(i=1;i<=5;i++){
			for(j=1;j<=5-i;j++){
					System.out.print(" ");
			}
				for(k=1;k<=2*i-1;k++){
                    if(k==1||k==2*1-1||i==5){
                        System.out.print("*");
                    }
					    System.out.print("  ");
				    }
			    System.out.println();
		    }
		}
	}
