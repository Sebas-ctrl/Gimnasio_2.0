<template id="formUsuario">
    <div class="min-h-screen bg-gray-100 text-gray-900 flex justify-center">
        <div class="max-w-screen-xl m-0 sm:m-10 bg-white shadow sm:rounded-lg flex justify-center flex-1">
            <div class="lg:w-1/2 xl:w-5/12 p-6 sm:p-12">
                <div class="mt-12 flex flex-col items-center">
                    <h1 class="text-2xl xl:text-3xl font-extrabold">
                        Registrarse
                    </h1>
                    <div class="w-full flex-1 mt-8 grid-cols-2">
                        <div class="gap-1">
                            <Usuario />
                            <Persona />
                            <a href="/" class="col-span-2">
                                <button
                                    class="mt-5 tracking-wide font-semibold bg-blue-700 text-gray-100 w-full py-4 rounded-lg hover:bg-blue-900 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none col-span-2">
                                    <svg class="w-6 h-6 -ml-2" fill="none" stroke="currentColor" stroke-width="2"
                                        stroke-linecap="round" stroke-linejoin="round">
                                        <path d="M16 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2" />
                                        <circle cx="8.5" cy="7" r="4" />
                                        <path d="M20 8v6M23 11h-6" />
                                    </svg>
                                    <span class="ml-3 uppercase">
                                        Registrar
                                    </span>
                                </button>
                            </a>
                            <p class="mt-6 text-xs text-gray-600 text-center col-span-2">
                                I agree to abide by templatana's
                                <a href="#" class="border-b border-gray-500 border-dotted">
                                    Terms of Service
                                </a>
                                and its
                                <a href="#" class="border-b border-gray-500 border-dotted">
                                    Privacy Policy
                                </a>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="flex-1 bg-gray-500 text-center hidden lg:flex ">
                <div class="m-12 xl:m-16 w-10/12 bg-contain bg-center bg-no-repeat "
                    style="background-image: url('https://i.ibb.co/pdP0hjc/logo-gimnasio.png');">
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