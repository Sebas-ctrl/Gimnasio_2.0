<template>
    <form>
        <input
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5 col-span-2"
            type="email" placeholder="Email"
        />
        <input
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5 "
            type="password" placeholder="Contraseña"
        />
        <input
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5 "
            type="password" placeholder="Repetir contraseña"
        />
        <a href="/" class="col-span-2" >
            <button
                class="mt-5 tracking-wide font-semibold bg-red-700 text-gray-100 w-full py-4 rounded-lg hover:bg-red-900 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none col-span-2">
                <svg class="w-6 h-6 -ml-2" fill="none" stroke="currentColor" stroke-width="2"
                    stroke-linecap="round" stroke-linejoin="round">
                    <path d="M16 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2" />
                    <circle cx="8.5" cy="7" r="4" />
                    <path d="M20 8v6M23 11h-6" />
                </svg>
                <span class="ml-3 ">
                    Sign Up
                </span>
            </button>
        </a>
    </form>
</template>