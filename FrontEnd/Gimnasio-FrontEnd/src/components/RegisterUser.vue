<template id="formUsuario">
    <div class="min-h-screen bg-gray-100 text-gray-900 flex justify-center">
    <div class="max-w-screen-xl m-0 sm:m-10 bg-white shadow sm:rounded-lg flex justify-center flex-1">
        <div class="lg:w-1/2 xl:w-5/12 p-6 sm:p-12">
            <div class="mt-12 flex flex-col items-center">
                <h1 class="text-2xl xl:text-3xl font-extrabold">
                    Sign up
                </h1>
                <div class="w-full flex-1 mt-8 grid-cols-2">
                    <div class="grid grid-rows-2 grid-cols-2 gap-1">
                        
                    </div>
                </div>
            </div>
        </div>
        <div class="flex-1 bg-gray-500 text-center hidden lg:flex ">
            <div class="m-12 xl:m-16 w-10/12 bg-contain bg-center bg-no-repeat "
                style="background-image: url('https://i.ibb.co/pdP0hjc/logo-gimnasio.png');"
                >
            </div>
        </div>
    </div>
</div>
</template>

<script>
    import Persona from './Persona.vue';
    import Usuario from './Usuario.vue';

    export default {
        components: {
            Persona,
            Usuario
        }
    }

</script>