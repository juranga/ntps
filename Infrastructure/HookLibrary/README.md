# Creating Hooks for the System
***

#### Hook Function Guideline

0. Hooks must contain a function that receives packet as a parameter and be named as the file's name.

    ```python 
        def hook_name(packet):
    ```

1. Hooks can be coded in any language as long as they return the following 2 arguments in order:

    a. Packet of NFQUEUE Packet class

    b. String Keyword of the following:

    `Forward`: The packet will be set to forward at the end of this hook's execution. The packet will not be stored in the intercept queue, and will not go through other hooks.

   `Drop`: The packet's verdict will be set to dropped at the end of this hook's execution. The packet will not be stored in the intercept queue, and will not go through other hooks.

   `Modification`: This keyword signals that only modifications were done to the packet. The packet will then be
        stored in the intercept queue upon completion of all remaining hooks, as long as "Modification" continues to be the keyword throughout all executions. Otherwise, see `Forward` or `Drop`.

2. Any Hooks that do not return these 2 arguments will be nulled.

3. It is suggested to check the 4 hooks available in the Hook Directory to help guide hook creation.
    
