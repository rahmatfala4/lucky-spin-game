// Google AdMob Configuration
// NOTE: Jangan commit App ID aplikasi (APPLICATION_ID) ke repo — simpan di env vars.
// Unit iklan (ad unit) boleh disimpan di repo, tetapi untuk fleksibilitas gunakan env vars.

export const ADMOB_CONFIG = {
  publisherId: process.env.NEXT_PUBLIC_ADMOB_PUBLISHER_ID ?? "pub-4097764438032261",
  rewardAdUnitId:
    process.env.NEXT_PUBLIC_ADMOB_REWARD_AD_UNIT_ID ?? "ca-app-pub-4097764438032261/2278791277",
  rewardAmount: Number(process.env.NEXT_PUBLIC_ADMOB_REWARD_AMOUNT ?? 500),
};
