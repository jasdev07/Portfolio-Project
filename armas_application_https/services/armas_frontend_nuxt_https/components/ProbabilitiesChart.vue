<template>
  <div class="flex flex-nowrap overflow-x-auto py-2">
    <div v-for="(value, key) in probabilities" :key="key"
         class="flex-shrink-0 min-w-0 p-1 border border-gray-300 rounded-lg shadow-sm mx-2"
         :class="{'border-yellow-500 border-4': value === highestValue}"
         :style="getColorForCategory(value)">
      <span class="text-xs lg:text-sm text-gray-800 truncate">{{ key }}: {{ value.toFixed(2) }}%</span>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    probabilities: Object,
  },
  computed: {
    highestValue() {
      return Math.max(...Object.values(this.probabilities));
    },
    minValue() {
      return Math.min(...Object.values(this.probabilities));
    }
  },
  methods: {
    getColorForCategory(value) {
      const hue = 45; // Hue for yellow
      const range = 90 - 50; // Lightness range now reversed
      const scale = 1 - (value - this.minValue) / (this.highestValue - this.minValue); // Invert scale for value
      const lightness = 50 + scale * range; // Calculate inverted lightness
      return { backgroundColor: `hsl(${hue}, 100%, ${lightness}%)` };
    }
  }
}
</script>
